# from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render  # , redirect
from django_countries import countries
from . import models, forms


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
    country = request.GET.get("country")
    print(f"country: {country}")
    if country:
        form = forms.SearchForm(request.GET)

        if form.is_valid():
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            room_type = form.cleaned_data.get("room")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            bedrooms = form.cleaned_data.get("bedrooms")
            beds = form.cleaned_data.get("beds")
            baths = form.cleaned_data.get("baths")
            instant_book = form.cleaned_data.get("instant")
            superhost = form.cleaned_data.get("superhost")
            amenities = form.cleaned_data.get("amenities")
            facilities = form.cleaned_data.get("facilities")

            # print(f"form.city: {city}")
            # print(f"form.country: {country}")
            # print(f"form.room_type: {room_type}")
            # print(f"form.price: {price}")
            # print(f"form.guests: {guests}")
            # print(f"form.bedrooms: {bedrooms}")
            # print(f"form.beds: {beds}")
            # print(f"form.baths: {baths}")
            # print(f"form.instant_book: {instant_book}")
            # print(f"form.superhost: {superhost}")
            # print(f"form.amenities: {amenities}")
            # print(f"form.facilities: {facilities}")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city"] = city
            if country is not None:
                filter_args["country"] = country
            if room_type is not None:
                filter_args["room_type"] = room_type
            if price is not None:
                filter_args["price"] = price
            if guests is not None:
                filter_args["guests"] = guests
            if bedrooms is not None:
                filter_args["bedrooms"] = bedrooms
            if beds is not None:
                filter_args["beds"] = beds
            if baths is not None:
                filter_args["baths"] = baths
            if instant_book is True:
                filter_args["instant_book"] = True
            if superhost is True:
                filter_args["host__superhost"] = True

            for amenity in amenities:
                filter_args["amenities"] = amenity

            for facility in facilities:
                filter_args["facilities"] = facility

            print(f"filter_args: {filter_args}")

            rooms = models.Room.objects.filter(**filter_args)
    else:
        form = forms.SearchForm()
        rooms = []

    return render(request, "rooms/search.html", {"form": form, "rooms": rooms})
