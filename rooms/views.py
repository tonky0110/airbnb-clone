# from django.utils import timezone
from django.views.generic import ListView, DetailView

# from django.http import Http404
from django.shortcuts import render  # , redirect

from django_countries import countries

# from django.urls import reverse
from . import models


# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room  # 모델
    paginate_by = 10  # 페이지 사이즈
    paginate_orphans = 5  # 맨 마지막 페이지의 개수가 n개보다 작으면 전페이지에서 모두 조회
    ordering = "pk"  # 정렬순
    context_object_name = "rooms"

    # def get_context_data(self, **kwargs):
    #     context = super().get_ context_data(**kwargs)
    #     # context = {}
    #     now = timezone.now()
    #     context["now"] = now
    #     return context


# def room_detail(request, pk):
#     try:

#         room = models.Room.objects.get(pk=pk)
#         print(room)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home"))
#         raise Http404()


# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.detail/DetailView/
class RoomDetail(DetailView):

    """ Room Detail Definition """

    model = models.Room


def search(request):
    print(request.GET)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    # print(request)
    # print(f"city: {city}")
    # print(f"countries: {countries}")
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
