import scrapy
from pathlib import Path

keys = ['team_name', 'year', 'wins', 'losses', 'ot-losses', 'win-pct', 'goals-for', 'goals-against', 'diff']

class FormSpider(scrapy.Spider):
    name="form_spider"
    start_urls = [
        "https://www.scrapethissite.com/pages/forms/"
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"q": "New York"},
            callback=self.form_filled
        )

    def form_filled(self, response):
        rows = response.xpath("//tr[contains(@class, 'team')]")
        for row in rows:
            values = row.xpath('td/text()').getall()
            values = [x.strip() for x in values]
            yield dict(zip(keys, values))

