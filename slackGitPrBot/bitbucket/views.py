import hashlib
import hmac
import json

from django.http import HttpResponse
from rest_framework import views

from bitbucket.ParseBitBucketWebHook import ParseBitBucketWebHook


# Create your views here.

class Webhook(views.APIView):

    def post(self, request):
        event_key = request.headers['X-Event-Key']
        print(json.dumps({**request.headers}, indent=4))
        print(f"X-Event-Key={event_key}")
        print(json.dumps(request.data, indent=4))
        secret = "Gweujpr3edH1cvEE"
        hash_object = hmac.new(
            secret.encode("utf-8"),
            msg=request.encode("utf-8"),
            digestmod=hashlib.sha256,
        )
        calculated_signature = "sha256=" + hash_object.hexdigest()
        given_signature = request.headers['X-Hub-Signature']
        if not hmac.compare_digest(calculated_signature, given_signature):
            print(
                "Signatures do not match\nExpected signature:"
                f" {calculated_signature}\nActual: signature: {given_signature}"
            )
        else:
            print("Signatures match")
        if event_key == "pullrequest:comment_created":
            ParseBitBucketWebHook.parse_comment(request.data)
        elif event_key == 'pullrequest:changes_request_created':
            pass
        elif event_key == 'pullrequest:approved':
            pass
        return HttpResponse("Hello, world. You're at the bitbucket webhook index.")
