import scrapy


class CochescomSpider(scrapy.Spider):
    name = 'cochescom'
    allowed_domains = ['coches.com']
    start_urls = ['http://coches.com/']

    def parse(self, response):
        pass
