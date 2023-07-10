import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

# Phone -> Camera -> App -> API -> CAMERA
# Application programming interface
# REST APIs -> Web API

# Part 1
# Performing an HTTP GET request to the specified endpoint
# get_response = requests.get(endpoint)

# Printing the raw text response received from the GET request
# print(get_response.text)

# Difference
# Regular HTTP requests typically return HTML content
# REST API HTTP requests usually return data in JSON format (or XML)
# JSON (JavaScript Object Notation) is similar to Python dictionaries


# Printing the JSON response received from the GET request
# print(get_response.json())


# Part 2
# Specifying the endpoint URL
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything/"


# Performing an HTTP GET request to the endpoint and sending a JSON payload
# get_response = requests.get(endpoint, json={"query": "Hello World"})  # Content-Type : 'application/json'

# Content-Type : 'application/x-www-form-urlencoded'
# get_response = requests.get(endpoint, data={"query": "Hello World"}) # Alternative: Sending form-encoded data

# Printing the JSON response received from the GET request
# print(get_response.json())

# Printing the status code of the response
# print(get_response.status_code)


# Final

endpoint = "http://localhost:8000/api/"  # "http://127.0.0.1:8000/"
get_response = requests.get(
    endpoint, params={"abc": 123}, json={"query": "Hello World!"}
)

print(get_response.json())
# print(get_response.status_code)

# we can also set params directly to endpoints like this
# endpoint = "http://localhost:8000/api/?this_arg=this_value"
# endpoint = "http://localhost:8000/api/?abc=123"
