from django.contrib import admin
from django.urls import path, include

from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("board/", include("board.urls")),
    path("member/", include("member.urls")),
]
