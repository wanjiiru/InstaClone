from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile
from .forms import ProfileForm


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'home.html',{})


@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile.user = current_user
            print(profile)
            profile.__repr__()
    else:
        profile_form=ProfileForm()



    return render(request, 'profile/new.html', {'profile_form':profile_form,'profile':profile})


@login_required(login_url='/accounts/login/')
def display_profile(request, profile_id):
    profile = Profile.objects.get(belongs_to_id=profile_id)

    return render(request,'profile/profile.html',{"profile":profile})