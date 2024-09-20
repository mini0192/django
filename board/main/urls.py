from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='list'),
    path('post/', views.PostCreateView.as_view(), name='post'),
    path('save/', views.SaveView.as_view(), name='save'),
    path('<int:pk>/', views.DetailsView.as_view(), name="details")
]
