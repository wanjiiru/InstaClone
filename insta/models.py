from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField


# Create your models here.



class Profile(models.Model):
    profile_pic =ImageField(blank = True,manual_crop='1080x800')
    bio = models.CharField(max_length=255,blank=True)
    belongs_to= models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return str(self.belongs_to)


    def profile_save(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile


class Image(models.Model):
    pic=ImageField(manual_crop='1080x800')
    name= models.CharField(max_length=55)
    caption = models.TextField(blank=True)
    likes=models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_user_images(cls, profile):
        images = Image.objects.filter(profile__pk=profile)
        return images




