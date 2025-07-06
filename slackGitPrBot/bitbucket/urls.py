from django.urls import path

from bitbucket.views import Webhook

urlpatterns = [path(r'', Webhook.as_view())]
