from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import  UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout

# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             messages.success(
#                 request, f'Signup Succesful {username}!You May Now Log In!')
#             form.save()
#             return redirect('userlogin')
#     else:
#         form = UserSignupForm()
#     return render(request, 'users/signup.html', {'form': form})

@login_required
def profile(request, username):
    """
    Renders the users profile, checks that the user matches profile user
    """
    # user = get_object_or_404(User, username=username)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
    }

    return render(request, "users/profile.html", context)

@login_required
def edit_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f'Your Profile has been updated!')
        
            return redirect("profile", username=user.username)

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'user':user,
    }

    return render(request, 'users/edit_profile.html', context)

@login_required()
def delete_profile(request, username):
    
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(
            request, f"Your account has been deleted { user.username }"
        )
        return redirect("dublineats-home")

    context = {"username": username}
    return render(request, "users/edit_profile.html", context)
