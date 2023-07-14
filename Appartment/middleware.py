from analytics.utils import get_client_ip
from django.shortcuts import get_object_or_404
from analytics.models import Visitor,number_of_visits

class VisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
       

        response = self.get_response(request)
        
        ip = get_client_ip(request)
        check = Visitor.objects.filter(ip_address=ip)
        if len(check) == 0:
            
            Visitor.objects.create(
                ip_address = ip
            )
            
            count = number_of_visits.objects.all().first()
            count.visits += 1
            count.save()

        # Code to be executed for each request/response after
        # the view is called.

        return response