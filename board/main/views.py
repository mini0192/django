from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Board
from .forms import BoardForm
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model = Board
    template_name = "list.html"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        return Board.objects.order_by("id")

class PostCreateView(generic.CreateView):
    model = Board
    form_class = BoardForm
    def get_success_url(self) -> str:
        return reverse_lazy("list")
    
class DetailsView(generic.DetailView):
    model = Board
    template_name = "details.html"

class SaveView(generic.TemplateView):
    template_name = "save.html"