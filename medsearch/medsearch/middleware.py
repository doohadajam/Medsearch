from django.shortcuts import redirect
from django.urls import reverse

class SearchLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            return self.get_response(request)

        response = self.get_response(request)
        # Increment the search count if a search request was made
        if 'q' in request.GET or 'q' in request.POST:

            request.session['search_count'] = request.session.get('search_count', 0) + 1

        return response
