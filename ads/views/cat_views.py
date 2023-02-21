from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Category
from ads.permissions import AdsCreatePermission
from ads.serializers.cat_serializer import CatListSerializer, CatDetailSerializer, CatCreateSerializer, \
    CatUpdateSerializer, CatDeleteSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatListSerializer

    def get(self, request, *args, **kwargs):
        cat_name = request.GET.get('name', None)
        if cat_name:
            self.queryset = self.queryset.filter(
                name__icontains=cat_name
            )

        return super().get(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CatDetailSerializer
    permission_classes = [IsAuthenticated]



class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatCreateSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatUpdateSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatDeleteSerializer
    permission_classes = [IsAuthenticated, AdsCreatePermission]
