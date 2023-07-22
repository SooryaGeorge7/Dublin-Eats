from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm



def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Signup Succesful {username}!You May Now Log In!')
            form.save()
            return redirect('dublineats-home')
    else:
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'form': form})

