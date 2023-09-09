from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout


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
    """
    Renders the edit profile page, checks that the user matches profile user
    , the form is prepopulated with existing data and also checks whether the forms 
    are valid before saving to database
    """
    user = request.user
    # user = User.objects.get(username=username)
    profile_user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=profile_user)

    if profile.user != user and not user.is_superuser:
        messages.error(
            request, "You are not authorized to edit this profile."
        )
        return redirect(reverse(
            "profile", kwargs={'username': username})
        )

    if request.method == 'POST':
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f'Your Profile has been updated!'
            )
            return redirect("profile", username=user.username)

    else:
        user_form = UserUpdateForm(instance=profile_user)
        profile_form = ProfileUpdateForm(instance=profile_user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'user': user,
    }

    return render(request, 'users/edit_profile.html', context)


@login_required()
def delete_profile(request, username):
    """
    Allows delete profile functionality that deletes a profile 
    and its account
    """
    user = request.user
    profile_user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=profile_user)
    # user = get_object_or_404(User, username=username)
    if not user.is_superuser and profile.user != user:
        messages.error(
            request, "You are not authorized to delete this review."
        )
        return redirect(reverse(f'{restaurant.category}'))

    if request.method == "POST":
        if not user.is_superuser:
            logout(request)
        profile_user.delete()

        if user.is_superuser:
            messages.success(
                request, f"account has been deleted "
            )
        else:
            messages.success(
                request,
                f"Your account has been deleted { user.username }"
            )
        return redirect("dublineats-home")

    context = {"username": username}
    return render(request, "users/edit_profile.html", context)
