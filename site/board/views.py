from django.shortcuts import render, redirect, get_object_or_404
from .models import Board

def index(request):
    return render(request, "index.html", {})

def save(request):
    if request.method == 'GET':
        return render(request, "save.html", {})
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board(title = title, content = content)
        board.save()

        return redirect("findAll")
    
def findAll(request):
    boards = Board.objects.all()
    return render(request, "findAll.html", {"boards": boards})

def findById(request, id):
    board = get_object_or_404(Board, id=id)
    return render(request, "findById.html", {"board": board})

def updateById(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == 'GET':
        return render(request, "update.html", {"board": board})
    
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect("findById", id=id)


def deleteById(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == "POST":
        board.delete()
        return redirect("findAll")
