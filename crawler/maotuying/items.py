# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaotuyingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location_id = scrapy.Field()
    display_name = scrapy.Field()
    url = scrapy.Field()
    cover_image = scrapy.Field()
    reviews_count = scrapy.Field()
    tags_desc = scrapy.Field()
    address = scrapy.Field()
    review_rating = scrapy.Field()
    feature_reviews = scrapy.Field()
