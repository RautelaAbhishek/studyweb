from logging import RootLogger
from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name':'Study Room 1' },
#     {'id':2, 'name':'Study Room 2' },
#     {'id':3, 'name':'Study Room 3' },
#     {'id':4, 'name':'Study Room 4' },
#     {'id':5, 'name':'Study Room 5' },
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html',context)

def createRoom(request):
    
    context = {}
    return render(request, 'base/room_form.html', context)