# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjRentItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    metroInfo = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    type1 = scrapy.Field()
    type2 = scrapy.Field()
    floor = scrapy.Field()
    decoration = scrapy.Field()
    builtYear = scrapy.Field()
    area = scrapy.Field()
    toward = scrapy.Field()
    heating = scrapy.Field()
    cellName = scrapy.Field()
    houseUrl= scrapy.Field()
    cellUrl = scrapy.Field()
    lastVisit = scrapy.Field()
    visitIn7Days = scrapy.Field()
    totalVisits = scrapy.Field()
    houseAddr = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    cellPropertyFee = scrapy.Field()
    cellBuildingsNum = scrapy.Field()
    cellHousesNum = scrapy.Field()
    cellBuiltYear = scrapy.Field()
    cellBuildingType = scrapy.Field()
    cellHouseType = scrapy.Field()
    cellSecHouseAvgPrice = scrapy.Field()
    cellSecHouseNum = scrapy.Field()
    cellSecHouseSoldHis = scrapy.Field()
    cellAddr = scrapy.Field()
    cellHousePriceNote = scrapy.Field()
