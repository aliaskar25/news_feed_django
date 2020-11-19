from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse


class User(AbstractUser):
    follows = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False, blank=True
    )
    password = models.CharField(max_length=69)

    def __str__(self):
        return self.username

    def follow(self, user_id):
        user = User.objects.get(id=user_id)
        user.add(self)
        user.save()
        return reverse('user_detail_url', kwargs={'pk': self.id})


class Blog(models.Model):
    name = models.CharField(max_length=69, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = f'{self.user.username}\' blog'
        super(Blog, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_blog(sender, instance, created, *args, **kwargs):
    if created:
        blog = Blog.objects.create(user=instance)
        instance.blog = blog
        instance.save()