# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import IpProxyPoolItem

class ProxySpiderSpider(CrawlSpider):


    name = 'proxy_spider'
    allowed_domains = ['ip84.com']
    start_urls = ['http://ip84.com/gn']

    rules = (
        #跟随下一页链接
        Rule(LinkExtractor(restrict_xpaths="//a[@class='next_page']"),follow=True),
        #对所有链接中含有"/gn/数字"的链接调用parse_item函数进行数据提取并过滤重复链接
        Rule(LinkExtractor(allow=r'/gn/\d+',unique=True), callback='parse_item'),
    )

    def parse_item(self, response):
        print 'Hi, this is an item page! %s' % response.url
        item=IpProxyPoolItem()

        for proxy in response.xpath("//table[@class='list']/tr[position()>1]"):

            ip=proxy.xpath("td[1]/text()").extract_first()
            port=proxy.xpath("td[2]/text()").extract_first()
            location1=proxy.xpath("td[3]/a[1]/text()").extract_first()
            location2=proxy.xpath("td[3]/a[2]/text()").extract_first()
            level=proxy.xpath("td[4]/text()").extract_first()
            type = proxy.xpath("td[5]/text()").extract_first()
            speed=proxy.xpath("td[6]/text()").extract_first()
            item['ip_port']=(ip if ip else "")+":"+(port if port else "")
            item['type']=(type if type else "")
            item['level']=(level if level else "")
            item['location']=(location1 if location1 else "")+" "+(location2 if location2 else "")
            item['speed']=(speed if speed else "")
            item['source']=response.url
            return item
