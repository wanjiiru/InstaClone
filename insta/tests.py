from django.test import TestCase

# Create your tests here.
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from .models import Image, Profile, Comment


class ImageTestClass(TransactionTestCase):
    """test class for Image model"""

    def setUp(self):

        self.user = User.objects.create_user("testuser", "secret")

        self.new_profile = Profile(profile_pic='profiles/profile.jpg',
                                   bio="this is a test bio",
                                   owner=self.user)
        self.new_profile.save()

        self.new_image = Image(image='test.jpeg',
                               caption="image", owner=self.new_profile)

    def test_instance_true(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
