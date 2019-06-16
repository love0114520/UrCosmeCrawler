# -*- coding: utf-8 -*-
from UrCosmeCrawler.settings import Session
from UrCosmeCrawler.models.brand import Brand
from UrCosmeCrawler.models.product import Product
from UrCosmeCrawler.models.review import Review
from UrCosmeCrawler.models.tag import Tag
from UrCosmeCrawler.models.product_tags_mapping import ProductTagsMapping
from UrCosmeCrawler.models.series import Series
import UrCosmeCrawler.items as items

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BrandPipeline(object):
    session = None

    def open_spider(self, spider):
        self.session = Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        if isinstance(item, items.Brand):
            brand = Brand(id=item['id'], name=item['name'],
                          follow_number=item['follow_number'])
            self.session.merge(brand)
            self.session.commit()
        return item


class ProductPipeline(object):
    session = None

    def open_spider(self, spider):
        self.session = Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        if isinstance(item, items.Product):
            product = Product(id=item['id'], name=item['name'], brand_id=item['brand_id'],
                              category_depth_1_tag_id=item['category_depth_1_tag_id'],
                              category_depth_2_tag_id=item['category_depth_2_tag_id'],
                              category_depth_3_tag_id=item['category_depth_3_tag_id'],
                              series_id=item['series_id'], price=item['price'], volume=item['volume'],
                              release_date=item['release_date'])
            category_depth_1_tag = Tag(id=item['category_depth_1_tag_id'], name=item['category_depth_1_tag_name']) if item['category_depth_1_tag_id'] is not None else None
            category_depth_2_tag = Tag(id=item['category_depth_2_tag_id'], name=item['category_depth_2_tag_name']) if item['category_depth_2_tag_id'] is not None else None
            category_depth_3_tag = Tag(id=item['category_depth_3_tag_id'], name=item['category_depth_3_tag_name']) if item['category_depth_3_tag_id'] is not None else None
            series = Series(id=item['series_id'], name=item['series_name']) if item['series_id'] is not None else None
            item_tags = item['tags']
            tags = []
            for tag_id in item_tags:
                tags.append(Tag(tag_id, item_tags[tag_id]))
            if category_depth_1_tag is not None:
                self.session.merge(category_depth_1_tag)
            if category_depth_2_tag is not None:
                self.session.merge(category_depth_2_tag)
            if category_depth_3_tag is not None:
                self.session.merge(category_depth_3_tag)
            if series is not None:
                self.session.merge(series)
            for tag in tags:
                self.session.merge(tag)
            self.session.merge(product)
            for tag in tags:
                self.session.merge(ProductTagsMapping(product.id, tag.id))
            self.session.commit()
        return item


class ReviewPipeline(object):
    session = None

    def open_spider(self, spider):
        self.session = Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        if isinstance(item, items.Review):
            review = Review(id=item['id'], user_skin=item['user_skin'], user_age=item['user_age'],
                            publish_date=item['publish_date'], update_date=item['update_date'],
                            content=item['content'], product_id=item['product_id'])
            self.session.merge(review)
            self.session.commit()
        return item
