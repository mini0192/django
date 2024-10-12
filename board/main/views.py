from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Board
from .forms import BoardForm
from django.urls import reverse_lazy

# def list(request):
#     if request.method == "GET":
#         board = Board.objects.all()
#         return render(request, "main/list.html", {"board_list": board})
    
#     elif request.method == "POST":
#         board = Board()

#         board.title = request.POST['title']
#         board.content = request.POST['content']

#         board.save()
        
#         return render(request, "main/list.html", {})

def save(request):
    return render(request, "main/save.html", {})

def create(request):
    if request.method == "POST":

        board = Board()
        board.title = request.POST["title"]
        board.content = request.POSST["content"]

        board.save()


def list(request):
    board = Board.objects.all()
    con = {"board_list": board}
    return render(request, "list.html", con)


def detail(request, id):
    board = Board.objects.get(id=id)
    con = {"board": board}
    return render(request, "detail.html", con)