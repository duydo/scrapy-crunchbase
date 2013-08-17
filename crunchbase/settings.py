# Scrapy settings for linkedin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os

BOT_NAME = 'crunchbase'

SPIDER_MODULES = ['crunchbase.spiders']
NEWSPIDER_MODULE = 'crunchbase.spiders'

DOWNLOADER_MIDDLEWARES = {
    'crunchbase.middleware.CustomHttpProxyMiddleware': 543,
    'crunchbase.middleware.CustomUserAgentMiddleware': 545,
}

########### Item pipeline
#ITEM_PIPELINES = ["crunchbase.pipelines.CrunchbasePipeline",]

###########

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'crunchbase (+http://www.yourdomain.com)'

# Enable auto throttle
AUTOTHROTTLE_ENABLED = True

COOKIES_ENABLED = False

# Set your own download folder
DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "download_file")
#DOWNLOAD_FILE_FOLDER = '/tmp/crunchbase/download'

LOG_ENABLED = True
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_IP = 8

DEFAULT_REQUEST_HEADERS = { 'Referer': 'http://crunchbase.com/companies'}

