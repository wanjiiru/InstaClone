from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField


# Create your models here.



class Profile(models.Model):
    profile_pic = ImageField(blank=True, manual_crop = '1080x800')
    bio = models.CharField(max_length=255,blank=True)
    belongs_to = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return str(self.belongs_to)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    pic = ImageField(blank=True,manual_crop='1080x800')
    name= models.CharField(max_length=55)
    caption = models.TextField(blank=True)
    likes=models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE())


