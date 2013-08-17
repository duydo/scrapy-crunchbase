# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.conf import settings
from scrapy import log
from os import path
import os
import codecs
import sys

class CrunchbasePipeline(object):
    def process_item(self, item, spider):
        yield item
