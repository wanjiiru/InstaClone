from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile
from .forms import ProfileForm,ImageForm


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    return render(request,'home.html',{"all_images":all_images,"user":current_user})


@login_required(login_url='accounts/login/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()


    return render(request,'image.html',{"form":form})


@login_required(login_url='/login')
def profile(request):
    current_user = request.user.id
    profile_details = Profile.objects.filter(id=current_user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile =profile_form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        profile_form=ProfileForm()



    return render(request, 'profile/new.html', {'profile_details':profile_details,'profile_form':profile_form})


@login_required(login_url='/accounts/login/')
def display_profile(request, profile_id):
    profile=User.objects.filter(id=profile_id)
    profile_details = Profile.get_by_id(id=profile_id)
    images = Image.get_profile_images(profile_id)
    print(images)

    return render(request,'profile/profile.html',{"profile_details":profile_details,"profile":profile,"images":images})