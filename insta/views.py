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
    this_list = []
    for image in all_images:
        this_list.append((image,image.likes))
        print(this_list)
    return render(request,'home.html',{"all_images":this_list,"user":current_user})


@login_required(login_url='accounts/login/')
def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.profile = request.user
            add.save()
            print(add)
            return redirect('profile')
    else:
        form = ImageForm()


    return render(request,'image.html',{"form":form})


@login_required(login_url='/login')
def profile(request):
    current_user = request.user
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



    return render(request, 'profile/new.html', {'profile_form':profile_form,'profile':profile})


@login_required(login_url='/accounts/login/')
def display_profile(request, profile_id):
    profile = Profile.objects.get(belongs_to_id=profile_id)

    return render(request,'profile/profile.html',{"profile":profile})