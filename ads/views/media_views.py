# import json
#
# from django.core.paginator import Paginator
# from django.http import JsonResponse, Http404
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import UpdateView, ListView, DetailView, DeleteView, CreateView
#
# from ads.models import Media
# from hm_27_1 import settings
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class MediaListView(ListView):
#     model = Media
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         search_text = request.GET.get("text", None)
#         if search_text:
#             self.object_list = self.object_list.filter(text=search_text)
#
#         paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#
#         advertisements = []
#         for image in page_obj:
#             advertisements.append({
#                 "id": image.id,
#                 "name": image.name,
#                 "image_url": image.image.url if image.image else None
#             })
#
#             response = {
#                 "items": advertisements,
#                 "num_pages": paginator.num_pages,
#                 "total": paginator.count
#             }
#         return JsonResponse(response, safe=False)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class MediaDetailView(DetailView):
#     model = Media
#
#     def get(self, request, *args, **kwargs):
#         try:
#             image = self.get_object()
#         except Http404:
#             return JsonResponse({'error': 'Not found'}, status=404)
#         return JsonResponse({
#             "id": image.id,
#             "name": image.name,
#             "image_url": image.image.url if image.image else None
#         })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class MediaCreateView(CreateView):
#     model = Media
#     fields = ["name", "image"]
#
#     def post(self, request, *args, **kwargs):
#         image_cat = json.loads(request.body)
#
#         image_ = Media.objects.create(
#             name=image_cat["name"],
#         )
#
#         return JsonResponse({
#             "id": image_.id,
#             "name": image_.name,
#         })
#
#
# @method_decorator(csrf_exempt, name="dispatch")########
# class MediaUplodateView(UpdateView):
#     model = Media
#     fields = ["name", "image"]
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#
#         self.object.image = request.FILES["image"]
#         self.object.save()
#
#         return JsonResponse({
#             "id": self.object.id,
#             "name": self.object.name,
#             "image_url": self.object.image.url if self.object.image else None
#         })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class MediaDeleteView(DeleteView):
#     model = Media
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({"status": "данные удаленны"}, status=200)
