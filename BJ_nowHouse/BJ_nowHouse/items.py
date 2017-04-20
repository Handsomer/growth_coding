# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BjNowhouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project_name = scrapy.Field()
    local_place = scrapy.Field()
    publish_date = scrapy.Field()

    use_for = scrapy.Field()
    build_area = scrapy.Field()
    build_in_area = scrapy.Field()
    sale_for_build = scrapy.Field()
    sale_for_build_in = scrapy.Field()