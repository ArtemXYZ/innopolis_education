from asincs.aiohttp_session import RESTAsyncRequest
from asincs.aiosever import Aiofiler
from asincs.sitemap import SitemapHandler
from asincs.winter import Winter


class Parser:

    def __init__(self):
        self._filer = Aiofiler()
        self._arequest = RESTAsyncRequest()
        
        self.sitemap = SitemapHandler(self._arequest)
        self.winter  = Winter()


