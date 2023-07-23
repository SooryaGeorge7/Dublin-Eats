from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserSignupForm


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Signup Succesful {username}!You May Now Log In!')
            form.save()
            return redirect('userlogin')
    else:
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'form': form})


def profile(request):
    """
    Renders the users profile, checks that the user matches profile user
    """
    # user = get_object_or_404(User, username=username)

    profile = Profile.objects.get(user=request.user)

    context = {
        "profile": profile,
    }

    return render(request, "users/profile.html", context)

