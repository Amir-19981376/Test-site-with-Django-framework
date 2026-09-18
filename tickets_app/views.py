from django.shortcuts import render
from django.template.defaultfilters import title
from .models import Ticket


def add_ticket(request):
    title =request.GET.get('title')
    body = request.GET.get('body')
    if title and body:
        Ticket.objects.create(title=title,body=body)

    return render(request, 'tickets_app/add_ticket.html')
