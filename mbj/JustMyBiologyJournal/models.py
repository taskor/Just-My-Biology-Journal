from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField(max_length=500, null=True)
    date = models.DateField()

# End of file
