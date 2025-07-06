from django.http import HttpResponse
from rest_framework import views

from bitbucket.ParseBitBucketWebHook import ParseBitBucketWebHook  # noqa: F841


# Create your views here.

class Webhook(views.APIView):

    def post(self, request):
        # event_key = request.headers['X-Event-Key']
        # print(json.dumps({**request.headers}, indent=4))
        # print(f"X-Event-Key={event_key}")
        # print(json.dumps(request.data, indent=4))
        secret = "Gweujpr3edH1cvEE"  # noqa: F841
        print(1)
        print(2)
        print(3)
        print(4)
        print(5)
        print(6)
        print(1)
        # if event_key == "pullrequest:comment_created":
        #     ParseBitBucketWebHook.parse_comment(request.data)
        # elif event_key == 'pullrequest:changes_request_created':
        #     pass
        # elif event_key == 'pullrequest:approved':
        #     pass
        return HttpResponse("Hello, world. You're at the bitbucket webhook index.")
