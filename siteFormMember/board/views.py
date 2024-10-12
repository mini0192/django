from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import SaveForm

def index(request):
    return render(request, "index.html", {})

def save(request):
    if request.method == 'GET':
        form = SaveForm()
        return render(request, "board/save.html", {"form": form})
    
    if request.method == 'POST':
        form = SaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("findAll")
    
def findAll(request):
    boards = Board.objects.all()
    return render(request, "board/findAll.html", {"boards": boards})

def findById(request, id):
    board = get_object_or_404(Board, id=id)
    return render(request, "board/findById.html", {"board": board})

def updateById(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == 'GET':
        form = SaveForm(instance=board)
        return render(request, "board/update.html", {"form": form, "board": board})
    
    if request.method == 'POST':
        form = SaveForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect("findById", id=id)

def deleteById(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == "POST":
        board.delete()
        return redirect("findAll")
