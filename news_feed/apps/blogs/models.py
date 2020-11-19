from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=69, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = f'{self.user.username}\' blog'
        super(Blog, self).save(*args, **kwargs)
