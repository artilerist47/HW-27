import json

from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import User, Location
from hm_27_1 import settings


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        search_text = request.GET.get("text", None)
        if search_text:
            self.object_list = self.object_list.filter(text=search_text)

        paginator = Paginator(self.object_list.select_related('location'), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        user_ = []
        for user in page_obj.object_list:
            user_.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "locations": [user.location.name if user.location else ""],
            })

        response = {
            "items": user_,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": [user.location.name if user.location else ""],
            'published_ads': User.objects.get(id=kwargs['pk']).ad_set.filter(is_published=True).count()
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "role", "age", "locations"]

    def post(self, request, *args, **kwargs):
        user = json.loads(request.body)

        location, _ = Location.objects.get_or_create(name=user["locations"])

        user_ = User.objects.create(
            username=user["username"],
            password=user["password"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            role=user["role"],
            age=user["age"],
            location=location
        )

        return JsonResponse({
            "id": user_.id,
            "username": user_.username,
            "first_name": user_.first_name,
            "last_name": user_.last_name,
            "role": user_.role,
            "age": user_.age,
            "locations": location.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "age"]#, "location"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user = json.loads(request.body)
        self.object.username = user["username"]
        self.object.password = user["password"]
        self.object.first_name = user["first_name"]
        self.object.last_name = user["last_name"]
        self.object.age = user["age"]
        # self.object.location.name = user.location.name["location"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "username": self.object.username,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "age": self.object.age,
            "locations": self.object.location.name if self.object.location else "",
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "???????????????????????? ????????????"}, status=200)



