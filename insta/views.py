from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'home.html',{})


@login_required(login_url='/login')
def profile(request):
    current_user=request.user
    user_details=Profile.objects.filter(belongs_to = current_user.id).all()

    return render(request,'profile/profile.html',{"user_details":user_details})
