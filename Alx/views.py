from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from .forms import CreateUserForm, LoginForm


from django.contrib import messages

from Alx.forms import CreateUserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def starterpage(request):
    return render(request,'starter-page.html')

def servicepage(request):
    return render(request,'service-details.html')


def home(request):
    return render(request,'register.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success("Account created successfully")
            return redirect('login')
    return render(request, 'register.html', {'form': form })

def Userlogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,  data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User = authenticate(request, username=username, password=password)

            if User is not None:
              login(request, User)
              messages.success('You are now logged in as {username}')
              return redirect('index')

            return render(request, 'login.html', {'form': form})






