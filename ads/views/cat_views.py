import json

from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Category
from ads.serializers.cat_serializer import CatListSerializer, CatDetailSerializer, CatCreateSerializer, \
    CatUpdateSerializer, CatDeleteSerializer
from hm_27_1 import settings


# def index(request):
#     if request.method == "GET":
#         return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatListSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CatDetailSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatCreateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatUpdateSerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatDeleteSerializer
