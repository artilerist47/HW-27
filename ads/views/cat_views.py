import json

from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ads.models import Category
from ads.serializers.cat_serializer import CatListSerializer, CatDetailSerializer, CatCreateSerializer
from hm_27_1 import settings


# def index(request):
#     if request.method == "GET":
#         return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatListSerializer
    # model = Category
    #
    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #
    #     search_text = request.GET.get("text", None)
    #     if search_text:
    #         self.object_list = self.object_list.filter(text=search_text)
    #
    #     self.object_list = self.object_list.order_by("name")
    #
    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
    #     page_number = request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #
    #     # cat = []
    #     # for category in page_obj:
    #     #     cat.append({
    #     #         "id": category.id,
    #     #         "name": category.name,
    #     #
    #     #     })
    #
    #     response = {
    #         "items": CatListSerializer(page_obj, many=True).data,
    #         "num_pages": paginator.num_pages,
    #         "total": paginator.count
    #     }
    #     return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
# class CategoryDetailView(DetailView):
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CatDetailSerializer
    # model = Category
    #
    # def get(self, request, *args, **kwargs):
    #     try:
    #         category = self.get_object()
    #     except Http404:
    #         return JsonResponse({'error': 'Not found'}, status=404)
    #
    #     # return JsonResponse({
    #     #     "id": category.id,
    #     #     "name": category.name},
    #     # )
    #     return JsonResponse(CatDetailSerializer(category).data)


# @method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatCreateSerializer
    # model = Category
    # fields = ["name"]
    #
    # # def post(self, request, *args, **kwargs):
    # #     cat_data = json.loads(request.body)
    # #
    # #     category = Category.objects.create(
    # #         name=cat_data["name"],
    # #     )
    # #
    # #     return JsonResponse({
    # #         "id": category.id,
    # #         "name": category.name,
    # #     })
    # def post(self, request, *args, **kwargs):
    #     cat_data = CatCreateSerializer(data=json.loads(request.body))
    #     if cat_data.is_valid():
    #         cat_data.save()
    #     else:
    #         return JsonResponse(cat_data.errors)
    #
    #     return JsonResponse(cat_data.data)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        # cat_data = CatUpdateSerializer(data=json.loads(request.body))
        # if not cat_data.is_valid():
        #     cat_data.update(cat_data.data)
        # else:
        #     return JsonResponse(cat_data.errors)
        #
        # return JsonResponse(cat_data.data)
        super().post(request, *args, **kwargs)

        cat_data = json.loads(request.body)
        self.object.name = cat_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "категория удаленна"}, status=200)
