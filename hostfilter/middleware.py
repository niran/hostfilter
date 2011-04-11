import re

from django.conf import settings
from django.http import Http404

from .models import Host


HOST_META_FIELDS = ('HTTP_HOST', 'SERVER_NAME')


class HostFilterMiddleware(object):
    def __init__(self):
        self.main_hostname = getattr(settings, 'HOSTFILTER_MAIN_HOSTNAME',
            None)

    def process_request(self, request):
        for field in HOST_META_FIELDS:
            if getattr(request, 'hostname', None) is not None:
                break
            if field in request.META:
                request.hostname = request.META[field]

        if not hasattr(request, 'hostname'):
            # If we couldn't find a hostname at all, just let users see the
            # site.
            return
        
        if self.main_hostname and request.hostname == self.main_hostname:
            # Allow all requests to the main hostname.
            return

        try:
            host = Host.objects.get(hostname=request.hostname)
        except Host.DoesNotExist:
            raise Http404

        if not re.match(host.allowed_pattern, request.path):
            raise Http404
