import collections

my_list = []
class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        global my_list
        if my_list:
            if my_list[-1] == "end of request":
                my_list = []
        my_list.append(request)
        response = self.get_response(request)
        return response