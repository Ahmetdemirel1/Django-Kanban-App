from django.contrib import admin
from core.models import *





class KanbanAdmin(admin.ModelAdmin):
    pass


admin.site.register(KanbanModel, KanbanAdmin)