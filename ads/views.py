from django.http import JsonResponse


def index(request):
    if request.method == "GET":
        return JsonResponse({"status": "ok"}, status=200)