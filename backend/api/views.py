import json
from django.http import JsonResponse, HttpResponse

"""
def api_home(request, *args, **kwargs):
    # The request object represents the incoming HTTP request
    # from the client to the server
    # HttpRequest is a Django-specific class that provides
    # various attributes and methods to access request data
    
    # Print the available attributes and methods of the request object
    print(dir(request))
    
    # Access the raw request body data (byte string of JSON data)
    body = request.body
    
    # Create an empty dictionary to store the parsed JSON data
    data = {}
    
    try:
        # Attempt to parse the JSON data into a Python dictionary
        data = json.loads(body)  # Convert the JSON data into a Python dict
    except:
        pass
    
    # Print the keys and values of the parsed JSON data
    print(data.keys)
    print(data)
    
    # Return a JSON response with a message as the API response
    return JsonResponse({"message": "Yahallo! This is my first Django API response!"})
    
    # Print the headers of the request
    print(request.headers)
    
    # Print the GET parameters of the request
    print("request.get", request.GET)
    
    # Print the POST parameters of the request
    print("request.post", request.POST)
    
    # Add the GET parameters, headers, and content type to the data dictionary
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    
    # Return a JSON response with the data dictionary as the API response
    return JsonResponse(data)
"""

# Using Models
from product.models import Product

# Import the Product model from the product app's models.py file

"""
def api_home(request, *args, **kwargs):
    # Retrieve a random product from the database
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # Populate the data dictionary with the retrieved product's attributes
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
        # Perform serialization to convert the model data into JSON format
        # and return it as the response to the client
    return JsonResponse(data)
"""


from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "price"])
    return HttpResponse(data)
