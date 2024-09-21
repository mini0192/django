from django.contrib import admin
from django.urls import path, include
from pybo import views

app_name = 'index'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls'))
]
