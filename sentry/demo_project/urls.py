from django.conf.urls import url

from .views import exception_view, logging_view

urlpatterns = [
    url(r'^exception-demo/$', exception_view),
    url(r'^logging-demo/$', logging_view),
]
