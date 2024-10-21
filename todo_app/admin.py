from django.contrib import admin
from .models import TodoGroup,TodoItem
# Register your models here.
admin.site.register(TodoGroup)
admin.site.register(TodoItem)