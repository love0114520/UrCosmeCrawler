import re

import scrapy

import UrCosmeCrawler.items as items
from UrCosmeCrawler.settings import Pattern
from UrCosmeCrawler.settings import base_url
from UrCosmeCrawler.spiders.products_spider import ProductsSpider

brand_list = '/brand-list'


class BrandsSpider(scrapy.Spider):
    name = "brands"

    def start_requests(self):
        yield scrapy.Request(url=base_url + brand_list, callback=self.parse)

    def parse(self, response):
        for brand in response.css(Pattern.Brand.brand_url):
            yield response.follow(url=base_url + brand.get(), callback=self.parse_brand_page)

    def parse_brand_page(self, response):
        id = re.search(Pattern.Brand.id, response.url).group(1)
        name = response.css(Pattern.Brand.name).get()
        try:
            follow_number = int(response.css(
                Pattern.Brand.follow_number).re(Pattern.Brand.follow_number_extractor)[0].replace(",", ""))
        except:
            follow_number = 0

        item = items.Brand()
        item['id'] = id
        item['name'] = name
        item['follow_number'] = follow_number
        yield response.follow(url=base_url + '/brands/' + id + '/products', callback=ProductsSpider().parse)
        yield item
