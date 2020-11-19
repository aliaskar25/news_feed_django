from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.blogs.models import Blog


class User(AbstractUser):
    follows = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False, blank=True
    )
    password = models.CharField(max_length=69)
    blog = models.OneToOneField(
        Blog, on_delete=models.CASCADE, null=True, blank=True
    )


    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def create_blog(sender, instance, created, *args, **kwargs):
    if created:
        blog = Blog.objects.create(user=instance)
        instance.blog = blog
        instance.save()
