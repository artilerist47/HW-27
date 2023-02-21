from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.permissions import AdsCreatePermission
from ads.serializers.ad_serializer import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDeleteSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        adv_text = request.GET.get('name', None)
        if adv_text:
            self.queryset = self.queryset.filter(
                name__icontains=adv_text
            )
        adv_text = request.GET.get('author_id', None)
        if adv_text:
            self.queryset = self.queryset.filter(
                author__id__icontains=adv_text
            )
        adv_text = request.GET.get('author', None)
        if adv_text:
            self.queryset = self.queryset.filter(
                author__username__icontains=adv_text
            )
        adv_text = request.GET.get('price', None)
        if adv_text:
            self.queryset = self.queryset.filter(
                price__icontains=adv_text
            )
        adv_text = request.GET.get('description', None)
        if adv_text:
            self.queryset = self.queryset.filter(
                description__icontains=adv_text
            )
        adv_text = request.GET.get('category_id', None)
        if adv_text:
            self.queryset = self.queryset.filter(
                category__id__icontains=adv_text
            )
        adv_text = request.GET.get('is_published', None)
        if adv_text:
            self.queryset = self.queryset.filter(
                is_published__icontains=adv_text
            )

        return super().get(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdvertisementsCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated]


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
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category.id,
            "image": self.object.image.url if self.object.image else None
        })

    permission_classes = [IsAuthenticated]


class AdvertisementsDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer
    permission_classes = [IsAuthenticated]
