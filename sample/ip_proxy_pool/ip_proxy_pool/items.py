# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class IpProxyPoolItem(scrapy.Item):

    ip_port = scrapy.Field()
    type = scrapy.Field()
    level = scrapy.Field()
    country = scrapy.Field()
    location = scrapy.Field()
    speed = scrapy.Field()
    source = scrapy.Field()
