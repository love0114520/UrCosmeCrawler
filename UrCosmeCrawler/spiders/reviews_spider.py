import datetime
import re

import scrapy

import UrCosmeCrawler.items as items
from UrCosmeCrawler.settings import Pattern
from UrCosmeCrawler.settings import base_url

product_list = '/reviews'


class ReviewsSpider(scrapy.Spider):
    name = "reviews"

    def parse(self, response):
        for review in response.css(Pattern.Review.review_url):
            yield response.follow(url=base_url + review.get(), callback=self.parse_review_page)

        next_page = response.css(Pattern.Review.next_page).get()
        if next_page is not None:
            yield response.follow(url=base_url + next_page, callback=self.parse)

    def parse_review_page(self, response):
        id = re.search(Pattern.Review.id, response.url).group(1)
        author_review_status = response.css(Pattern.Review.author_review_status).get()
        author_status_matcher = re.search(Pattern.Review.author_status_extractor, author_review_status)
        user_skin = author_status_matcher.group(1)
        user_age = author_status_matcher.group(2)
        review_date_and_page_view = response.css(Pattern.Review.review_date_and_page_view).get()
        review_date_matcher = re.search(Pattern.Review.review_date_extractor, review_date_and_page_view)
        publish_date = datetime.datetime.strptime(review_date_matcher.group(1), Pattern.Product.date_format)
        update_date = None
        if ',' in review_date_and_page_view:
            update_date = datetime.datetime.strptime(review_date_matcher.group(2), Pattern.Product.date_format)
        content = re.sub(Pattern.Review.review_content_tag_replace, '', ''.join(
            response.css(Pattern.Review.review_content).extract()))
        product_id = response.css(Pattern.Review.product_id).re(Pattern.Review.product_id_extractor)[0]

        item = items.Review()
        item['id'] = id
        item['user_skin'] = user_skin
        item['user_age'] = user_age
        item['publish_date'] = publish_date
        item['update_date'] = update_date
        item['content'] = content
        item['product_id'] = product_id
        yield item
