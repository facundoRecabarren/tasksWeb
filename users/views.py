from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,ProfileForm,UpdateUser,UpdateProfile

# https://stackoverflow.com/questions/54490783/how-to-add-new-fields-in-django-user-model
def newUser(request):
    if request.method == 'POST':
        User_form = UserRegisterForm(request.POST)
        Profile_form = ProfileForm(request.POST)
        if User_form.is_valid() and Profile_form.is_valid():
            user = User_form.save()
            Profile_form = Profile_form.save(commit=False)
            Profile_form.user = user
            Profile_form.save()

            username = User_form.cleaned_data.get('username')
            messages.success(request, f'Well Done {username}! Now you can Log In with your new Account')
            return redirect('login')
    else:
        User_form = UserRegisterForm()
        Profile_form = ProfileForm()
    return render(request, 'users/register.html', {'form1':User_form,'form2':Profile_form})

@login_required
def profile(request):
    if request.method == 'POST':
        update_user = UpdateUser(request.POST, instance=request.user)
        update_profile = UpdateProfile(request.POST, request.FILES, instance=request.user.usuarios)
        if update_profile.is_valid() and update_user.is_valid():
            update_user.save()
            update_profile.save()
            messages.success(request, f'Your account has been updated!!')
            #evitamos el mensaje al recargar la pagina de 'quieres volver a enviar los datos?'
            return redirect('tasks-profile')
    else:
        update_user = UpdateUser(instance=request.user)
        update_profile = UpdateProfile(instance=request.user.usuarios)
    context = {
        'styleFolder' : 'css/profile.css',
        'form1':update_user,
        'form2':update_profile
        }
    return render(request, 'users/profile.html',context)