from django.http import HttpResponse


class FirstMiddleware:
    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request):
        print("BEFORE 11111 MIDDLEWARE")
        response = self._get_response(request)
        print("AFTER 11111 MIDDLEWARE")
        return response

    def process_exception(self, request, exception):
        print(f"Exeption is:{exception}")
        return HttpResponse('Exception!')