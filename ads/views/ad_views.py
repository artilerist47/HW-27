import json

from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ad, User  # , Media
from hm_27_1 import settings


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        search_text = request.GET.get("text", None)
        if search_text:
            self.object_list = self.object_list.filter(text=search_text)

        self.object_list = self.object_list.order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        advertisements = []
        for ad_ in page_obj:
            advertisements.append({
                "id": ad_.id,
                "name": ad_.name,
                "author_id": ad_.author.id,
                # "author": ad_.author,
                "price": ad_.price,
                "description": ad_.description,
                "is_published": ad_.is_published,
                # "category_id": ad_.category.id,
                "image": ad_.image.url if ad_.image else None,

            })

            response = {
                "items": advertisements,
                "num_pages": paginator.num_pages,
                "total": paginator.count
            }
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad_ = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse({
            "id": ad_.id,
            "name": ad_.name,
            "author_id": ad_.author.id,
            # "author": ad_.author,
            "price": ad_.price,
            "description": ad_.description,
            "is_published": ad_.is_published,
            # "category_id": ad_.category_id_id,
            "image": ad_.image.url if ad_.image else None,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsCreateView(CreateView):
    model = Ad
    fields = ["id", "name", "author", "price", "description", "address", "is_published"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        author_username = ad_data['author']


        try:
            author = get_object_or_404(User, username=author_username)
        except Http404:
            return JsonResponse({'status': 'Author not found'}, status=404)

        advertiments = Ad.objects.create(
            name=ad_data["name"],
            author=author,
            price=ad_data["price"],
            description=ad_data["description"],
            is_published=ad_data["is_published"],
        )

        return JsonResponse({
            "id": advertiments.id,
            "name": advertiments.name,
            "author": advertiments.author.username,
            "price": advertiments.price,
            "description": advertiments.description,
            "is_published": advertiments.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsUpdateView(UpdateView):
    model = Ad
    fields = ["id", "name", "author", "price", "description"]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        ad_data = json.loads(request.body)
        instance.name = ad_data["name"]
        instance.author_id = ad_data["author_id"]
        instance.price = ad_data["price"]
        instance.description = ad_data["description"]
        instance.category_id = ad_data["category_id"]

        instance.save()

        return JsonResponse({
            "id": instance.id,
            "name": instance.name,
            "author": str(instance.author),
            "author_id": instance.author_id,
            "price": instance.price,
            "description": instance.description,
            "is_published": instance.is_published,
            "category_id": instance.category_id,
        })


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


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "данные удаленны"}, status=200)
