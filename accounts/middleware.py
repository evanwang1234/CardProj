"""
class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-My-Header'] = "my value"
        return response

MIDDLEWARE = [
    ...,
    'yourapp.middleware.MyMiddleware',
    ...,
]

"""