import scrapy
import json

class MovieSpider(scrapy.Spider):
    name = 'movies'

    def start_requests(self):
        base_url = "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=%s"
        for year in range(2010, 2016):
            yield scrapy.Request(url= base_url % year, callback=self.parse)

    def parse(self, response):
        items = json.loads(response.body)
        for item in items:
            yield item
