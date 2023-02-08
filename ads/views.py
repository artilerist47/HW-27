import json

from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def index(request):
    if request.method == "GET":
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        category = Category()

        category.name = cat_data["name"]
        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name},
        )


@method_decorator(csrf_exempt, name='dispatch')
class AdvertisementsView(View):
    def get(self, request):
        ads_ = Ad.objects.all()

        response = []
        for ad_ in ads_:
            response.append({
                "id": ad_.id,
                "name": ad_.name,
                "author": ad_.author,
                "price": ad_.price,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        ad_ = Ad()

        ad_.name = ad_data["name"]
        ad_.author = ad_data["author"]
        ad_.price = ad_data["price"]
        ad_.description = ad_data["description"]
        ad_.address = ad_data["address"]
        ad_.is_published = ad_data["is_published"]
        ad_.save()

        return JsonResponse({
            "id": ad_.id,
            "name": ad_.name,
            "author": ad_.author,
            "price": ad_.price,
            "description": ad_.description,
            "address": ad_.address,
            "is_published": ad_.is_published,
        })


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
            "author": ad_.author,
            "price": ad_.price,
            "description": ad_.description,
            "address": ad_.address,
            "is_published": ad_.is_published,
        })
