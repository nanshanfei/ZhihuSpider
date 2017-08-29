# -*- coding: utf-8 -*-
import scrapy
from urlparse import urljoin
from scrapy.http import Request
from ..items import LjRentItem
import re


class LianjiaSpiderSpider(scrapy.Spider):
    name = "lianjia_spider"
    allowed_domains = ["m.lianjia.com"]
    start_urls = ['http://m.lianjia.com/wh/zufang']
    id=2

    def parse(self, response):
        houseLst=response.xpath("//li[@class='pictext']")
        next_url="http://m.lianjia.com/wh/zufang/pg%s/" %(self.id)
        for house in houseLst:
            url=urljoin("http://m.lianjia.com",house.xpath("a/@href").extract_first())#房屋详情url
            yield Request(url,callback=self.parse_house_info)
        #开始爬取下一页
        self.id+=1
        yield Request(next_url, callback=self.parse)

    def parse_house_info(self,response):
        #使用xpath表达式提取房屋信息
        houseUrl = response.url
        metroInfo=response.xpath("//section[@class='page page_zufang has_fixbar']/div[@class='mod_box house_detail']/ul[@class='lists']/li[@class='li_item'][5]/div[@class='value box_col']/text()").extract_first()
        title=response.xpath("//h1[@class='house_title']/text()").extract_first()
        price=response.xpath("//span[@class='total_price']/em[@class='num']/text()").extract_first()
        type1=response.xpath("//li[@class='li_item'][1]/div[@class='value box_col'][1]/text()").extract_first()
        type2 = response.xpath("//li[@class='li_item'][4]/div[@class='value box_col'][2]/text()").extract_first()
        floor=response.xpath("//li[@class='li_item'][2]/div[@class='value box_col'][1]/text()").extract_first()
        decoration=response.xpath("//li[@class='li_item'][3]/div[@class='value box_col'][1]/text()").extract_first()
        builtYear=response.xpath("//li[@class='li_item'][4]/div[@class='value box_col'][1]/text()").extract_first()
        id=response.xpath("//section[@class='page page_zufang has_fixbar']/div[@class='mod_box house_detail']/ul[@class='lists']/li[@class='li_item'][6]/div[@class='value box_col']/text()").extract_first()
        area=response.xpath("//li[@class='li_item'][1]/div[@class='value box_col'][2]/text()").extract_first()
        toward=response.xpath("//li[@class='li_item'][2]/div[@class='value box_col'][2]/text()").extract_first()
        heating=response.xpath("//li[@class='li_item'][3]/div[@class='value box_col'][2]/text()").extract_first()
        cellName=response.xpath("//li[@class='li_item arrow']/a[@class='flexbox']/div[@class='value box_col']/text()").extract_first()
        cellUrl=urljoin("http://m.lianjia.com",response.xpath("//a[@class='flexbox']/@href").extract_first())
        lastVisit=response.xpath("//div[@class='mod_box house_record']/h3[@class='mod_tit']/small/span/text()").extract_first()
        visitIn7Days=response.xpath("//div[@class='data flexbox']/div[@class='box_col'][1]/strong/text()").extract_first()
        totalVisits=response.xpath("//div[@class='data flexbox']/div[@class='box_col'][2]/strong/text()").extract_first()
        houseAddr=response.xpath("//div[@class='mod_cont gap']/a/div[@class='location_desc']/text()").extract_first()
        lon_lat_url=response.xpath("//div[@class='mod_box location']/h3/a/@href").extract_first()
        #正则表达式提取非html文本中的数据
        longitude=re.search("pos=(.*?),",lon_lat_url).group(1)#正则表达式取经度
        latitude=re.search(",(.*?)&house_code",lon_lat_url).group(1)#正则表达式取纬度

        item=LjRentItem()
        #python的三目运算的用法
        #true_result if condition else false_result
        item['metroInfo']="" if id is None else metroInfo.strip()
        item['houseUrl']="" if id is None else houseUrl.strip()
        item['id'] = "" if id is None else id.strip()
        item['title'] = "" if title is None else title.strip()
        item['price'] = "" if price is None else price.strip()
        item['type1'] = "" if type1 is None else type1.strip()
        item['type2'] = "" if type2 is None else type2.strip()
        item['floor'] = "" if floor is None else floor.strip()
        item['decoration'] = "" if decoration is None else decoration.strip()
        item['builtYear'] = "" if builtYear is None else builtYear.strip()
        item['area'] = "" if area is None else area.strip()
        item['toward'] = "" if toward is None else toward.strip()
        item['heating'] = "" if heating is None else heating.strip()
        item['cellName'] = "" if cellName is None else cellName.strip()
        item['cellUrl'] = "" if cellUrl is None else cellUrl.strip()
        item['lastVisit'] = "" if lastVisit is None else lastVisit.strip()
        item['visitIn7Days'] = "" if visitIn7Days is None else visitIn7Days.strip()
        item['totalVisits'] = "" if totalVisits is None else totalVisits.strip()
        item['houseAddr'] = "" if houseAddr is None else houseAddr.strip()
        item['longitude'] = "" if longitude is None else longitude.strip()
        item['latitude'] = "" if latitude is None else latitude.strip()
        yield Request(cellUrl,callback=self.parse_cell_info,meta=item)#将item传给parse_cell_info

    def parse_cell_info(self,response):
        item=response.meta#接收传过来的item
        #提取小区信息
        cellPropertyFee=response.xpath("//li[@class='li_item'][1]/div[@class='box_col flexbox']/span[@class='value box_col']/text()").extract_first()
        cellBuildingsNum=response.xpath("//li[@class='li_item'][2]/div[@class='box_col flexbox'][1]/span[@class='value box_col']/text()").extract_first()
        cellHousesNum=response.xpath("//li[@class='li_item'][2]/div[@class='box_col flexbox'][2]/span[@class='value box_col']/text()").extract_first()
        cellBuiltYear=response.xpath("//ul[@class='lists']/li[@class='li_item'][3]/div[@class='box_col flexbox'][2]/span[@class='value box_col']/text()").extract_first()
        cellBuildingType=response.xpath("//li[@class='li_item'][5]/div[@class='box_col flexbox']/span[@class='value box_col']/text()").extract_first()
        cellHouseType=response.xpath("//ul[@class='lists']/li[@class='li_item'][6]/div[@class='box_col flexbox']/span[@class='value box_col']/text()").extract_first()
        cellSecHouseAvgPrice=response.xpath("//div[@class='mod_box house_chart']/h3[@class='chart_head']/span[@class='red']/text()").extract_first()
        cellSecHouseNum=response.xpath("//h3[@class='mod_tit'][1]/a[@class='arrow']/span[@class='red']/text()").extract_first()
        cellSecHouseSoldHis=response.xpath("//h3[@class='mod_tit'][2]/a[@class='arrow']/span[@class='red']/text()").extract_first()
        cellAddr=response.xpath("//div[@class='mod_box location']/div[@class='mod_cont']/a/div[@class='location_desc']/text()").extract_first()
        cellHousePriceNote=response.xpath("//div[@class='mod_box house_chart']/h3[@class='chart_head']/p/text()").extract_first()

        item['cellPropertyFee'] = "" if cellPropertyFee is None else cellPropertyFee.strip()
        item['cellBuildingsNum'] = "" if cellBuildingsNum is None else cellBuildingsNum.strip()
        item['cellHousesNum'] = "" if cellHousesNum is None else cellHousesNum.strip()
        item['cellBuiltYear'] = "" if cellBuiltYear is None else cellBuiltYear.strip()
        item['cellBuildingType'] = "" if cellBuildingType is None else cellBuildingType.strip()
        item['cellHouseType'] = "" if cellHouseType is None else cellHouseType.strip()
        item['cellSecHouseAvgPrice'] = "" if cellSecHouseAvgPrice is None else cellSecHouseAvgPrice.strip()
        item['cellSecHouseNum'] = "" if cellSecHouseNum is None else cellSecHouseNum.strip()
        item['cellSecHouseSoldHis'] = "" if cellSecHouseSoldHis is None else cellSecHouseSoldHis.strip()
        item['cellAddr'] = "" if cellAddr is None else cellAddr.strip()
        item['cellHousePriceNote'] = "" if cellHousePriceNote is None else cellHousePriceNote.strip()

        yield item
