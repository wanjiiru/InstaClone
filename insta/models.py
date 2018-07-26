from django.contrib.auth.models import User
from django.db import models
from pyuploadcare.dj.models import ImageField
from friendship.models import Friend,Follow,Block

# Create your models here.



class Profile(models.Model):
    profile_pic =ImageField( blank=True)
    bio = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return str(self.bio)


    def profile_save(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(owner=id)
        return profile

    @classmethod
    def get_profile_by_username(cls, owner):
        profiles = cls.objects.filter(owner__contains=owner)
        return profiles





class Image(models.Model):
    pic=ImageField(manual_crop='1080x800')
    name= models.CharField(max_length=55)
    caption = models.TextField(blank=True)
    likes=models.BooleanField(default=False)
    profile= models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return str(self.name)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk=profile)
        return images

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='comment')
    comment_owner = models.ForeignKey(User)
    comment= models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments

    def __str__(self):
        return str(self.comment)





