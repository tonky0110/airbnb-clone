# from django.utils import timezone
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render  # , redirect

# from django.urls import reverse
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room  # 모델
    paginate_by = 10  # 페이지 사이즈
    paginate_orphans = 5  # 맨 마지막 페이지의 개수가 n개보다 작으면 전페이지에서 모두 조회
    ordering = "pk"  # 정렬순
    context_object_name = "rooms"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context = {}
    #     now = timezone.now()
    #     context["now"] = now
    #     return context


def room_detail(request, pk):
    try:

        room = models.Room.objects.get(pk=pk)
        print(room)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()
