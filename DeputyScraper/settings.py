# Scrapy settings for DeputyScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'DeputyScraper'

SPIDER_MODULES = ['DeputyScraper.spiders']
NEWSPIDER_MODULE = 'DeputyScraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DeputyScraper (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['DeputyScraper.pipelines.MongoDBPipeline']

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "deputies"
MONGODB_COLLECTION = "basic_info"
