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
    creater = Profile.objects.get(belongs_to=current_user)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add = form.save()
            add.profile = creater
            add.save()
            print(add)
            return redirect('home')
    else:
        form = ImageForm()


    return render(request,'image.html',{"form":form})


@login_required(login_url='/login')
def profile(request,profile_id):
    current_user = request.user
    profile_details = User.objects.filter(id=profile_id).all()
    user = User.objects.get(id=current_user.id)
    if current_user.is_authenticated() and current_user.id == user.id:
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST,request.FILES)
            if profile_form.is_valid():
                profile.user = current_user
                print(profile)
                profile_form.save()
        else:
            profile_form=ProfileForm()



        return render(request, 'profile/new.html', {'profile_details':profile_details,'profile_form':profile_form })


@login_required(login_url='/accounts/login/')
def display_profile(request, profile_id):
    profile_details = Profile.objects.filter(belongs_to_id=profile_id).all()
    print(profile_details)

    return render(request,'profile/profile.html',{"profile_details":profile_details})