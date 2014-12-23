# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EducaragonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    coord = scrapy.Field()
    centro = scrapy.Field()
    curso = scrapy.Field()
    temas = scrapy.Field()
    url = scrapy.Field()
