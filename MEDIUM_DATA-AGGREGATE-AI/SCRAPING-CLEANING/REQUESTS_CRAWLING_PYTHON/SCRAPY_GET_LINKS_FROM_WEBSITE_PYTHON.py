#pip install scrapy

### IMPORT LIBRARIES ###

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy import Item
from scrapy import Field


class UrlItem(Item):
    url = Field()


class WikiSpider(CrawlSpider):
    name = 'wiki'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page/']

    rules = (
        Rule(LinkExtractor(), callback='parse_url'),
    )

    def parse_url(self, response):
        item = UrlItem()
        item['url'] = response.url

        return item
