from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventAddForm


def landing_page(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'index.html', context)

def event_details(request, event_title):
    event = get_object_or_404(Event, title=event_title)
    return render(request, 'event_details.html', {'event': event})

def add_event(request):
    if request.method == "POST":
        form = EventAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = EventAddForm()
    return render(request, 'add_event.html', {"form": form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        event.delete()
        return redirect('landing_page')
    return redirect('event_details', event_id=event_id)