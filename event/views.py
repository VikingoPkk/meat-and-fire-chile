from django.shortcuts import render
from .models import EventSection, Chef, Ticket

def home(request):
    sections = EventSection.objects.all()
    chefs = Chef.objects.all()
    tickets = Ticket.objects.all() # <--- AÑADIDO
    return render(request, 'index.html', {
        'sections': sections, 
        'chefs': chefs,
        'tickets': tickets
    })