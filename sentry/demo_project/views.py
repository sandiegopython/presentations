import logging
from django.http import HttpResponse

logger = logging.getLogger()


def exception_view(request):
    raise Exception("demo exception")


def logging_view(request):
    logger.error('There was some crazy error', exc_info=True, extra={
        # Optionally pass a request
        'request': request,
    })
    return HttpResponse("Logging demo response...")
