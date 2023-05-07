from django.contrib import admin
from .models import TodoListModel
from datetime import date

@admin.register(TodoListModel)
class TodoListModelAdmin(admin.ModelAdmin):
    list_display=('nome','dia','mes','modificado_em')
    list_editable=('dia','mes',)

