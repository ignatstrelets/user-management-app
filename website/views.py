from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
#initially it was : forms import SignUpForm, AddRecordForm 
""", AddRecordForm"""
"""from .models import Record"""
"""records = Record.objects.all()"""

def home(request):
#   """records = Record.objects.all()"""
    user = get_user_model()
    all_users = user.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
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
        #return render(request, 'home.html')
    #initially it was 'return render(request, 'home.html', {'records':records})' 



def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
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
            del selected_users_id[-1]
            print(selected_users_id)
            for id in selected_users_id:
                try:
                    u = User.objects.get(id = id)
                    u.is_active = False
                    u.save()
                    messages.success(request, "The User is Blocked")

                except Exception as e:
                    messages.error(request, e.message)
                    return redirect('home')

                return redirect('home')


def unblock_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_users_id = request.POST.getlist('boxes')
            del selected_users_id[-1]
            print (selected_users_id)
            for id in selected_users_id:
                try:
                    u = User.objects.get(id = id)
                    u.is_active = True
                    u.save()
                    messages.success(request, "The User is Unblocked")

                except Exception as e:
                    messages.error(request, e.message)
                    return redirect('home')

                return redirect('home') 

def delete_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_users_id = request.POST.getlist('boxes')
            del selected_users_id[-1]
            for id in selected_users_id:
                try:
                    u = User.objects.get(id = id)
                    u.delete()
                    messages.success(request, "The User is Deleted")

                except Exception as e:
                    messages.error(request, e.message)
                    return redirect('home')

                return redirect('home')

"""
def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
"""

# deletion of user (via toolbar)
"""
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home') 
"""    
"""
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save() 
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
"""

"""
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home') 
 """
