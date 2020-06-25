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
    # print(request.GET)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.get("amenities")
    s_facilities = request.GET.get("facilities")
    print(s_amenities, s_facilities)
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }
    # print(form)
    return render(request, "rooms/search.html", {**form, **choices},)
