from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/posts/', views.posts_list, name="posts_list"),
    path('dashboard/users/', views.user_list, name="user_list"),
    path('dashboard/user/create/', views.user_create, name="user_create"),
    path('dashboard/posts/create', views.create_post, name="create_post"),
]
