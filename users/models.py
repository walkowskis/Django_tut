from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
        # after change models is nessesary to make a migration
        # in terminal:
        # python manage.py makemigrations
        # and after that python manage.py migrate
        # register this model in users/admin.py
