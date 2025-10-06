from django.shortcuts import render
from django.db.models import Q
from .models import Room, Topic, Message

# Home page view
def home(request):
    q = request.GET.get('q', '')  # simpler than before

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()[:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q)
    )[:3]

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
        'room_messages': room_messages
    }
    return render(request, 'base/home.html', context)  # matches your tree

# Topics page view
def topicsPage(request):
    q = request.GET.get('q', '')
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})
