import json

from django.http import HttpResponse
from rest_framework import views


# Create your views here.

class Webhook(views.APIView):

    def post(self, request):
        print(json.dumps(request.data, indent=4))
        return HttpResponse("Hello, world. You're at the bitbucket webhook index.")