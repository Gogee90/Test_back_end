from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='media')


class BlogPost(models.Model):
    author = models.ForeignKey('Employee', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absloute_url(self):
        return reverse('blog_posts', kwargs={'pk': self.pk})