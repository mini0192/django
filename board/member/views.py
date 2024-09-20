from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", default = None)
        password = request.POST.get("password", default = None)

        print(username)
        print(password)

        user = authenticate(username = username, password = password)
        if user == None:
            print("로그인 실패")
        else:
            print("로그인 성공")

        return render(request, "login.html", {})

    else:
        return render(request, "login.html", {})