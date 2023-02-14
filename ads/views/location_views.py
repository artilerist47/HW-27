import json

from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from ads.models import Location
from hm_27_1 import settings


@method_decorator(csrf_exempt, name='dispatch')
class LocationListView(ListView):
    model = Location

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        search_text = request.GET.get("text", None)
        if search_text:
            self.object_list = self.object_list.filter(text=search_text)

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        loaction_ = []
        for ad_ in page_obj:
            loaction_.append({
                "id": ad_.id,
                "name": ad_.name,
                "lat": ad_.lat,
                "lng": ad_.lng,
            })

        response = {
            "items": loaction_,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)
