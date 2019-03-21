from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # validation data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"{username}, your account has been created. Let's get started!")
            # after that redirect to another webside
            return redirect('blog-home')
    else:
        # invalid request result empty form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
