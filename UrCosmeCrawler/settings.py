# -*- coding: utf-8 -*-
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Scrapy settings for UrCosmeCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'UrCosmeCrawler'

SPIDER_MODULES = ['UrCosmeCrawler.spiders']
NEWSPIDER_MODULE = 'UrCosmeCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'UrCosmeCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.8
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'UrCosmeCrawler.middlewares.UrcosmecrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'UrCosmeCrawler.middlewares.UrcosmecrawlerDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'UrCosmeCrawler.pipelines.BrandPipeline': 100,
    'UrCosmeCrawler.pipelines.ProductPipeline': 200,
    'UrCosmeCrawler.pipelines.ReviewPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

engine = db.create_engine('postgresql://appUser:pa$$word1234@localhost:5432/makeup')
Session = sessionmaker(bind=engine)
Base = declarative_base()
base_url = 'https://www.urcosme.com'


class Pattern(object):
    class Brand(object):
        brand_url = '#brands-list>.uc-container>.uc-brand-list-brands>.uc-brand-list-brand>a.uc-minor-link::attr(href)'
        id = r'https?://www\.urcosme\.com/brands/(\d+)/?.*'
        name = '.headline-title>span::text'
        follow_number = '.focus-count::text'
        follow_number_extractor = r'([\d,]+).+'

    class Product(object):
        product_url = '#append-products .product-infomation>.product-name>a.uc-minor-link::attr(href)'
        next_page = '#append-products>.pagination>a.next_page::attr(href)'
        id = r'https?://www\.urcosme\.com/products/(\d+)/?.*'
        name = '.uc-headline>div.headline-title.product-name::text'
        brand_id = '.uc-headline>.brand-name>a.uc-main-link::attr(href)'
        brand_id_extractor = r'.*/brands/(\d+).*'
        category_depth_1_tag_id = '.uc-product-details>.uc-product-detail:nth-child(4)>.detail-text>a.uc-main-link:nth-child(1)::attr(href)'
        category_depth_2_tag_id = '.uc-product-details>.uc-product-detail:nth-child(4)>.detail-text>a.uc-main-link:nth-child(3)::attr(href)'
        category_depth_3_tag_id = '.uc-product-details>.uc-product-detail:nth-child(4)>.detail-text>a.uc-main-link:nth-child(5)::attr(href)'
        category_depth_1_tag_name = '.uc-product-details>.uc-product-detail:nth-child(4)>.detail-text>a.uc-main-link:nth-child(1)::text'
        category_depth_2_tag_name = '.uc-product-details>.uc-product-detail:nth-child(4)>.detail-text>a.uc-main-link:nth-child(3)::text'
        category_depth_3_tag_name = '.uc-product-details>.uc-product-detail:nth-child(4)>.detail-text>a.uc-main-link:nth-child(5)::text'
        series_id = '.uc-product-details>.uc-product-detail:nth-child(3)>.detail-text>a.uc-main-link::attr(href)'
        series_id_extractor = r'.+\?series=(\d+)'
        series_name = '.uc-product-details>.uc-product-detail:nth-child(3)>.detail-text>a.uc-main-link::text'
        product_info_other = '.product-info-block>.product-info-others>.product-info-other'
        product_info_other_extractor = r'<div class="other-text">([^>]+)</div>'
        price_extractor = r'NT\$\s*(\d+)'
        release_date = '.product-info-block>.product-info-others>.product-info-other:nth_child(3)>.other-text::text'
        date_format = '%Y.%m.%d'
        tags_id = '.uc-product-details>.uc-product-detail:nth-child(5)>.detail-text>a.uc-main-link::attr(href)'
        tags_id_extractor = r'/tags/(\d+)'
        tags_name = '.uc-product-details>.uc-product-detail:nth-child(5)>.detail-text>a.uc-main-link::text'

    class Review(object):
        review_url = '#append-reviews>.uc-reviews>.uc-review>.review-content-container>a.review-content-top::attr(href)'
        next_page = '#append-reviews>.pagination>a.next_page::attr(href)'
        id = r'https?://www\.urcosme\.com/reviews/(\d+)/?.*'
        author_review_status = '.uc-container>.review-info>.author-info>.author-review-status>span::text'
        author_status_extractor = r'・([^・]+)・(\d+)歲'
        review_date_and_page_view = '.uc-container>.review-info>.author-info>.review-date-and-pageview>span::text'
        review_date_extractor = r'(\d{1,4}\.\d{1,2}\.\d{1,2}) 發表(?:, (\d{1,4}\.\d{1,2}\.\d{1,2}) 更新)?'
        review_content = '.uc-container>.review-content'
        review_content_tag_replace = r'<[^>]+>'
        product_id = '.uc-container>.product-actions>.product-img>a::attr(href)'
        product_id_extractor = r'/products/(\d+)'
