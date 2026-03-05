from django.contrib import admin
from .models import EventSection, Chef, Ticket

admin.site.register(Ticket)
@admin.register(EventSection)
class EventSectionAdmin(admin.ModelAdmin):
    list_display = ('type', 'title')

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'order')