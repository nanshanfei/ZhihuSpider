# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from model import Base,engine,loadSession
from model import proxy


class IpProxyPoolPipeline(object):
    #搜索Base的所有子类，并在数据库中生成表
    Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        a = proxy.Proxy(
            ip_port=item['ip_port'],
            type=item['type'],
            level=item['level'],
            location=item['location'],
            speed=item['speed'],
            source=item['source']
        )
        session = loadSession()
        session.add(a)
        session.commit()
        return item
