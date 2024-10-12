from django.contrib import admin
from .models import Board

# class BoardAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["title"]}),
#         ("Content", {"fields": ['content']})
#     ]

admin.site.register(Board)