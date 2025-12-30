import json

from django.http import HttpResponse
from rest_framework import views

from bitbucket.ParseBitBucketWebHook import ParseBitBucketWebHook
from bot_logging.setup_logger import Loggers

# Create your views here.

logger = Loggers.get_logger(logger_name="bitbucket_logging")[0]


class Webhook(views.APIView):

    def post(self, request):
        logger.info(request)
        logger.info(json.dumps({**request.headers}, indent=4))
        logger.info(json.dumps(request.data, indent=4))
        ParseBitBucketWebHook.verify_request(request)
        event_key = request.headers['X-Event-Key']
        if event_key == "pullrequest:comment_created":
            ParseBitBucketWebHook.parse_comment(request.data)
        elif event_key == 'pullrequest:changes_request_created':
            pass
        elif event_key == 'pullrequest:approved':
            pass
        else:
            raise Exception("No event key detected")
        return HttpResponse("Hello, world. You're at the bitbucket webhook index.")
