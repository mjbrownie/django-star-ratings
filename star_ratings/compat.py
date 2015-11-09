from django.utils import simplejson
from django.http import HttpResponse

try:
    from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
    from django.contrib.contenttypes.generic import GenericForeignKey

try:
    from django.http import JsonResponse
except ImportError:
    class JsonResponse(HttpResponse):
        """
            JSON response
        """
        def __init__(self, data, mimetype='application/json', status=None, content_type=None):
            super(JsonResponse, self).__init__(
                content=simplejson.dumps(data),
                mimetype=mimetype,
                status=status,
                content_type=content_type,
            )
