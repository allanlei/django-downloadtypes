from downloads.views import DownloadMixin


import zipfile
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
    

class ZippedResponseMixin(DownloadMixin):
    contenttype = 'application/zip'
    
    def get_compressed_contents(self, files=[]):
        buff = StringIO.StringIO()
        zip = zipfile.ZipFile(buff, 'w', zipfile.ZIP_DEFLATED)
        for name, content in files:
            zip.writestr(name, content)
        zip.close()
        buff.flush()
        contents = buff.getvalue()
        buff.close()
        return contents

#class TarGZResponseMixin(object):
#    pass
