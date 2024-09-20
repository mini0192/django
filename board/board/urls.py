from django.contrib import admin
from django.urls import path, include
from index.views import index
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('^__debug__/', include(debug_toolbar.urls)),
    path('', index),
    path('index', include('index.urls')),

    path('member/', include('member.urls')),
    path('board/', include('main.urls')),
]
