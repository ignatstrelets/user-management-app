from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    user = get_user_model()
    all_users = user.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'users':all_users})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def block_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_users_id = request.POST.getlist('boxes')
            caller_id = request.user.id
            selected_users_id.remove(str(caller_id))
            for id in selected_users_id:
                u = User.objects.get(id = id)
                u.is_active = False
                u.save()
                messages.success(request, "The User is Blocked")
            return redirect('home')


def unblock_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_users_id = request.POST.getlist('boxes')
            caller_id = request.user.id
            selected_users_id.remove(str(caller_id))
            for id in selected_users_id:
                u = User.objects.get(id = id)
                u.is_active = True
                u.save()
                messages.success(request, "The User is Unblocked")
            return redirect('home') 


def delete_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_users_id = request.POST.getlist('boxes')
            caller_id = request.user.id
            selected_users_id.remove(str(caller_id))
            for id in selected_users_id:
                u = User.objects.get(id = id)
                u.delete()
                messages.success(request, "The User is Deleted")
            return redirect('home')
