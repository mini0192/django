from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('save/', views.save, name='save'),
    path('board/', views.list),
    path('detail/<int:id>', views.detail),
    # path('post/', views.PostCreateView.as_view(), name='post'),
    # 
    # path('<int:pk>/', views.DetailsView.as_view(), name="details")
]
