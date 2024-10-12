from django.urls import path
from . import views

urlpatterns = [
    path("save", views.save, name="save"),
    path("<int:id>", views.findById, name="findById"),
    path("update/<int:id>", views.updateById, name="updateById"),
    path("delete/<int:id>", views.deleteById, name="delete"),
    path("", views.findAll, name="findAll"),
]