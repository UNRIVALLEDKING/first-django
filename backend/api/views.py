import json
from django.http import JsonResponse


# def api_home(request, *args, **kwargs):
# request -> HttpRequest -> Django
# print(dir(request))
# request.body
# body = request.body  # byte string of JSON data
# data = {}
# try:
# data = json.loads(body)  # string of JSON data -> Python Dict
# except:
# pass
# print(data.keys)
# print(data)
# return JsonResponse({"message": "Yahallo! This is my first Django API response!"})
# print(request.headers)
# print("request.get", request.GET)
# print("request.post", request.POST)
# data["params"] = dict(request.GET)
# data["headers"] = dict(request.headers)
# data["content_type"] = request.content_type
# return JsonResponse(data)


# Using Models

from product.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
        # model instance (model_data)
        # turn a python dict
        # return JSON to my client
        # serialization
    return JsonResponse(data)
