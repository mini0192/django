from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .form import Join, Login

def join(request):
    if request.method == "POST":
        form = Join(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print(form.errors)

    form = Join()
    return render(request, "member/join.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("index")
        else:
            print(form.errors)
    
    form = Login()
    return render(request, "member/login.html", {"form": form})
        
def logout(request):
    auth_logout(request)
    return redirect("index")
