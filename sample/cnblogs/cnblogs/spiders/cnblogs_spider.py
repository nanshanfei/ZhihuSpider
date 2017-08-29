#coding=utf-8
import re
import json
from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from cnblogs.items import *
from scrapy.crawler import CrawlerProcess

class CnblogsSpider(CrawlSpider):
    #定义爬虫的名称
    name = "CnblogsSpider"
    #定义允许抓取的域名,如果不是在此列表的域名则放弃抓取
    allowed_domains = ["cnblogs.com"]
    #定义抓取的入口url
    start_urls = [
        "http://www.cnblogs.com/rwxwsblog/default.html?page=1"
    ]
    # 定义爬取URL的规则，并指定回调函数为parse_item
    rules = [
        Rule(sle(allow=("/rwxwsblog/default.html\?page=\d{1,}")),
                         follow=True,
                         callback='parse_item')
    ]

    def parse_item(self, response):
        # items = []
        sel = Selector(response)
        page_url = response.url
        base_url = get_base_url(response)
        postTitle = sel.css('div.day div.postTitle')
        postCon = sel.css('div.postCon div.c_b_p_desc')
        for index in range(len(postTitle)):
            item = CnblogsItem()
            try:
                item['page_url'] = page_url
                item['title'] = postTitle[index].css("a").xpath('text()').extract()[0]
                item['link'] = postTitle[index].css('a').xpath('@href').extract()[0]
                item['listUrl'] = base_url
                item['desc'] = postCon[index].xpath('text()').extract()[0]
            except Exception,e:
                print(str(e))
            yield item
            # items.append(item)
        # return items
        
        
if '__name__' == '__main__':
    
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(CnblogsSpider)
    process.start()