from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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

    def save(self):
        # parent classes save method will be run when we save pic
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            # to change profil pic size
            output_size = (300, 300)
            img.thumbnail(output_size)
            # save to the same path
            img.save(self.image.path)
