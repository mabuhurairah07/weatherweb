# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CroncheckItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name = scrapy.Field()
    # id = scrapy.Field()
    city = scrapy.Field()
    curr_temp = scrapy.Field()
    pass
