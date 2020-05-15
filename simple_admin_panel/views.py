from django.shortcuts import render, redirect
from .models import BlogPost, Employee
from .forms import RegistrationForm, PostForm
from django.utils import timezone



# Create your views here.
def dashboard(request):
    return render(request, "simple_admin_panel/dashboard.html")


def posts_list(request):
    posts = BlogPost.objects.all()
    return render(request, "simple_admin_panel/blog_posts.html", {"posts": posts})


def user_list(request):
    users = Employee.objects.all()
    return render(request, "simple_admin_panel/user_list.html", {"users": users})


def user_create(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password']
            first_name = registration_form.cleaned_data['first_name']
            last_name = registration_form.cleaned_data['last_name']
            email = registration_form.cleaned_data['email']
            user = Employee.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.password2 = password
            user.save()
            return redirect('main_page')
    else:
        registration_form = RegistrationForm()
    return render(request, 'simple_admin_panel/user_create.html', {
        'registration_form': registration_form,
    })


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, "simple_admin_panel/create_post.html", {"form": form})
