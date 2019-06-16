import datetime
import re

import scrapy

import UrCosmeCrawler.items as items
from UrCosmeCrawler.settings import Pattern
from UrCosmeCrawler.settings import base_url
from UrCosmeCrawler.spiders.reviews_spider import ReviewsSpider

product_list = '/products'


class ProductsSpider(scrapy.Spider):
    name = "products"

    def parse(self, response):
        for product in response.css(Pattern.Product.product_url):
            yield response.follow(url=base_url + product.get(), callback=self.parse_product_page)

        next_page = response.css(Pattern.Product.next_page).get()
        if next_page is not None:
            yield response.follow(url=base_url + next_page, callback=self.parse)

    def parse_product_page(self, response):
        id = re.search(Pattern.Product.id, response.url).group(1)
        name = response.css(Pattern.Product.name).get()
        brand_id = response.css(Pattern.Product.brand_id).re(Pattern.Product.brand_id_extractor)[0]
        try:
            category_depth_1_tag_id = response.css(Pattern.Product.category_depth_1_tag_id).re(Pattern.Product.tags_id_extractor)[0]
        except:
            category_depth_1_tag_id = None
        try:
            category_depth_2_tag_id = response.css(Pattern.Product.category_depth_2_tag_id).re(Pattern.Product.tags_id_extractor)[0]
        except:
            category_depth_2_tag_id = None
        try:
            category_depth_3_tag_id = response.css(Pattern.Product.category_depth_3_tag_id).re(Pattern.Product.tags_id_extractor)[0]
        except:
            category_depth_3_tag_id = None
        category_depth_1_tag_name = response.css(Pattern.Product.category_depth_1_tag_name).get()
        category_depth_2_tag_name = response.css(Pattern.Product.category_depth_2_tag_name).get()
        category_depth_3_tag_name = response.css(Pattern.Product.category_depth_3_tag_name).get()
        try:
            series_id = response.css(Pattern.Product.series_id).re(Pattern.Product.series_id_extractor)[0]
        except:
            series_id = None
        series_name = response.css(Pattern.Product.series_name).get()

        product_info_others = response.css(Pattern.Product.product_info_other).getall()
        volume = None
        price = None
        release_date = None
        if product_info_others is not None and len(product_info_others) > 0:
            for product_info_other in product_info_others:
                if '容量' in product_info_other:
                    volume = re.search(Pattern.Product.product_info_other_extractor, product_info_other).group(1)
                elif '價格' in product_info_other:
                    price = re.search(Pattern.Product.product_info_other_extractor, product_info_other).group(1)
                elif '上市日期' in product_info_other:
                    release_date = datetime.datetime.strptime(
                        re.search(Pattern.Product.product_info_other_extractor, product_info_other).group(1),
                        Pattern.Product.date_format)

        tags_ids = response.css(Pattern.Product.tags_id).getall()
        for i in range(len(tags_ids)):
            tags_ids[i] = re.search(Pattern.Product.tags_id_extractor, tags_ids[i]).group(1)
        tags_names = response.css(Pattern.Product.tags_name).getall()
        tags = dict(zip(tags_ids, tags_names)) if tags_ids is not None else []
        item = items.Product()
        item['id'] = id
        item['name'] = name
        item['brand_id'] = brand_id
        item['category_depth_1_tag_id'] = category_depth_1_tag_id
        item['category_depth_2_tag_id'] = category_depth_2_tag_id
        item['category_depth_3_tag_id'] = category_depth_3_tag_id
        item['category_depth_1_tag_name'] = category_depth_1_tag_name
        item['category_depth_2_tag_name'] = category_depth_2_tag_name
        item['category_depth_3_tag_name'] = category_depth_3_tag_name
        item['series_id'] = series_id
        item['series_name'] = series_name
        item['volume'] = volume
        item['price'] = price
        item['release_date'] = release_date
        item['tags'] = tags
        yield response.follow(url=base_url + '/products/' + id + '/reviews', callback=ReviewsSpider().parse)
        yield item
