from django.db import models

from apps.users.models import Blog


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
