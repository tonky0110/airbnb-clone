from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room  # 모델
    paginate_by = 10  # 페이지 사이즈
    paginate_orphans = 5  # 맨 마지막 페이지의 개수가 n개보다 작으면 전페이지에서 모두 조회
    ordering = "created"  # 정렬순
