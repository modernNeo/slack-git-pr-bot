import json

from django.http import HttpResponse
from rest_framework import views

from bitbucket.ParseBitBucketWebHook import ParseBitBucketWebHook


# Create your views here.

class Webhook(views.APIView):

    def post(self, request):
        ParseBitBucketWebHook.verify_request(request)
        event_key = request.headers['X-Event-Key']
        print(json.dumps({**request.headers}, indent=4))
        print(f"X-Event-Key={event_key}")
        print(json.dumps(request.data, indent=4))
        if event_key == "pullrequest:comment_created":
            ParseBitBucketWebHook.parse_comment(request.data)
        elif event_key == 'pullrequest:changes_request_created':
            pass
        elif event_key == 'pullrequest:approved':
            pass
        print("", flush=True)
        return HttpResponse("Hello, world. You're at the bitbucket webhook index.")
