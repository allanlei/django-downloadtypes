from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured


class DownloadMixin(object):
    filename = None
    
    def get_filename(self):
        return self.filename

    def get_contenttype(self):
        if self.contenttype:
            contenttype = self.contenttype
        else:
            raise ImproperlyConfigured('Provide contenttype.')
        return contenttype

    def get_compressed_contents(self, files=[]):
        raise NotImplementedError

    def render_to_response(self, files=[]):
        response = HttpResponse(self.get_compressed_contents(files=files), mimetype=self.get_contenttype())
        filename = self.get_filename()
        if filename: response['Content-Disposition'] = 'filename=%s' % filename
        return response
