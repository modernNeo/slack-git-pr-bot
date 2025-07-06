import hashlib  # noqa: F401
import hmac  # noqa: F401
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
        # print(json.dumps(request.data, indent=4))
        secret = "Gweujpr3edH1cvEE"  # noqa: F841
        print(1)
        json_load = json.dumps(request.data)
        print(2)
        enc_load = f"{json_load}".encode("utf-8")  # noqa: F841
        print(3)
        # hash_object = hmac.new(  # noqa: F841
        #     secret.encode("utf-8"),
        #     msg=enc_load,
        #     digestmod=hashlib.sha256,
        # )
        print(4)
        # calculated_signature = "sha256=" + hash_object.hexdigest()  # noqa: F841
        print(5)
        given_signature = request.headers['X-Hub-Signature']  # noqa: F841
        print(6)
        # if not hmac.compare_digest(calculated_signature, given_signature):
        #     print(
        #         "Signatures do not match\nExpected signature:"
        #         f" {calculated_signature}\nActual: signature: {given_signature}"
        #     )
        # else:
        #     print("Signatures match")
        print(7)
        if event_key == "pullrequest:comment_created":
            ParseBitBucketWebHook.parse_comment(request.data)
        elif event_key == 'pullrequest:changes_request_created':
            pass
        elif event_key == 'pullrequest:approved':
            pass
        return HttpResponse("Hello, world. You're at the bitbucket webhook index.")
