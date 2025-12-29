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
        ParseBitBucketWebHook.verify_request(request)
        event_key = request.headers['X-Event-Key']
        logger.info(request.headers)
        logger.info(json.dumps({**request.headers}, indent=4))
        logger.info(f"X-Event-Key={event_key}")
        logger.info(request.data)
        logger.info(json.dumps(request.data, indent=4))
        if event_key == "pullrequest:comment_created":
            ParseBitBucketWebHook.parse_comment(request.data)
        elif event_key == 'pullrequest:changes_request_created':
            pass
        elif event_key == 'pullrequest:approved':
            pass
        return HttpResponse("Hello, world. You're at the bitbucket webhook index.")
