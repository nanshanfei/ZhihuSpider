# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi

class LjRentPipeline(object):
    def __init__(self):
        self.ids_seen = set()#初始化一个无序不重复集和ids_seen
        db_args = dict(
            host="127.0.0.1",  # 数据库主机ip
            db="test",  # 数据库名称
            user="root",  # 用户名
            passwd="123456",  # 密码
            charset='utf8',  # 数据库字符编码
            cursorclass=MySQLdb.cursors.DictCursor,  # 以字典的形式返回数据集
            use_unicode=True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **db_args)

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen or item['id']=="":#使用id作为i唯一主键
            raise DropItem("Duplicate or invalid item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            self.dbpool.runInteraction(self.insert_into_LJRent_raw, item)
            return item

    def insert_into_LJRent_raw(self, conn, item):
        sql_insert='''
        INSERT INTO LJRent_raw(
            id,
            metroInfo,
            title,
            price,
            type1,
            type2,
            floor,
            decoration,
            builtYear,
            area,
            toward,
            heating,
            houseUrl,
            cellName,
            cellUrl,
            lastVisit,
            visitIn7Days,
            totalVisits,
            houseAddr,
            longitude,
            latitude,
            cellPropertyFee,
            cellBuildingsNum,
            cellHousesNum,
            cellBuiltYear,
            cellBuildingType,
            cellHouseType,
            cellSecHouseAvgPrice,
            cellSecHouseNum,
            cellSecHouseSoldHis,
            cellAddr,
            cellHousePriceNote)
            VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
        ''' %(
            item['id'],
            item['metroInfo'],
            item['title'],
            item['price'],
            item['type1'],
            item['type2'],
            item['floor'],
            item['decoration'],
            item['builtYear'],
            item['area'],
            item['toward'],
            item['heating'],
            item['houseUrl'],
            item['cellName'],
            item['cellUrl'],
            item['lastVisit'],
            item['visitIn7Days'],
            item['totalVisits'],
            item['houseAddr'],
            item['longitude'],
            item['latitude'],
            item['cellPropertyFee'],
            item['cellBuildingsNum'],
            item['cellHousesNum'],
            item['cellBuiltYear'],
            item['cellBuildingType'],
            item['cellHouseType'],
            item['cellSecHouseAvgPrice'],
            item['cellSecHouseNum'],
            item['cellSecHouseSoldHis'],
            item['cellAddr'],
            item['cellHousePriceNote']
        )
        #print 'SQL:',sql_insert
        conn.execute(sql_insert)
