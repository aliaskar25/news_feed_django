from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from apps.users.models import Blog

from utils.send_notification import notification



class Post(models.Model):
    title = models.CharField(max_length=69)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='posts',
        null=True, 
    )

    def __str__(self):
        return self.title


@receiver(post_save, sender=Post)
def create_post(sender, instance, created, *args, **kwargs):
    if created:
        recepients = instance.blog.user.followers.values_list('email', flat=True)
        link = f'http://127.0.0.1:1234/{instance.id}/'
        notification(list(recepients), instance.title, link)
