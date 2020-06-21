from math import ceil
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    # rooms = paginator.get_page(page)
    rooms = paginator.page(int(page))
    # print(dir(rooms))
    return render(request, "rooms/home.html", {"page": rooms},)

