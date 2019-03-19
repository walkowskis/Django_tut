from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    # attribiutes -> different field in the databases
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete means if author will delete the post will also:
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # after that we should accep migration: python manage.py makemigrations

    def __str__(self):
        return self.title
