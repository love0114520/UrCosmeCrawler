# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Brand(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    follow_number = scrapy.Field()


class Product(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    brand_id = scrapy.Field()
    category_depth_1_tag_id = scrapy.Field()
    category_depth_2_tag_id = scrapy.Field()
    category_depth_3_tag_id = scrapy.Field()
    category_depth_1_tag_name = scrapy.Field()
    category_depth_2_tag_name = scrapy.Field()
    category_depth_3_tag_name = scrapy.Field()
    series_id = scrapy.Field()
    series_name = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()
    release_date = scrapy.Field()
    tags = scrapy.Field()


class Review(scrapy.Item):
    id = scrapy.Field()
    user_skin = scrapy.Field()
    user_age = scrapy.Field()
    publish_date = scrapy.Field()
    update_date = scrapy.Field()
    content = scrapy.Field()
    product_id = scrapy.Field()


class Series(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()


class Tag(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
