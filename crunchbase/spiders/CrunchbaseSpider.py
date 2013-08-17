from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.http import Request
# from scrapy import log
# from crunchbase.items import CrunchbaseItem
from os import path
from crunchbase.parser.CrunchbaseDataParser import CrunchbaseDataParser
import os
# from scrapy.conf import settings

# import urllib
# import string
# from bs4 import UnicodeDammit
# from linkedin.db import MongoDBClient

class CrunchbaseSpiderSpider(CrawlSpider):
    name = 'CrunchbaseSpider'
    allowed_domains = ['crunchbase.com']
    start_urls = [ "http://www.crunchbase.com/companies?c=%s" % s for s in "abcdefghijklmnopqrstuvwxyz"]
    
    rules = (
        Rule(SgmlLinkExtractor(allow=(r'company/([^\/])+$')), callback='parse_item', follow=True),
    )

    def __init__(self, **kwargs):
        super(CrunchbaseSpiderSpider, self).__init__()
        pass
    
    def parse_item(self, response):
        # log.msg(response.url);
        fn = self.filename(response)
        if not path.exists(fn) :
            x = HtmlXPathSelector(response)
            item = CrunchbaseDataParser.extract_item(x)
            #item['url_crunchbase'] = response.url
            self.save_to_file_system(response.body, fn);
            yield item

    def filename(self, response):
        fn = self.get_clean_file_name(response)
        if fn is None:
            return None
        fn = path.join(self.settings["DOWNLOAD_FILE_FOLDER"], fn)
        return fn
        
    def save_to_file_system(self, content, fn):
        """
        save the response folder
        """
        self.create_path_if_not_exist(fn)
        if not path.exists(fn):
            with open(fn, "w") as f:
                f.write(content)
    
    def get_clean_file_name(self, response):
        url = response.url
        return url.split("/")[-1] + ".html"

    def create_path_if_not_exist(self, filePath):
        if not path.exists(path.dirname(filePath)):
            os.makedirs(path.dirname(filePath))
            
