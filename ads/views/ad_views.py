import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad, User  # , Media
from ads.serializers.ad_serializer import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDeleteSerializer
from hm_27_1 import settings


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdvertisementsCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AdvertisementsUplodateView(UpdateView):
    model = Ad
    fields = ["name", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.id,
            # "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category.id,
            "image": self.object.image.url if self.object.image else None
        })


class AdvertisementsDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer
