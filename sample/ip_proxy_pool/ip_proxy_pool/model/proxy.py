# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,Integer,DateTime

from . import Base
import datetime
class Proxy(Base):
    __tablename__ = 'proxies'

    ip_port=Column(String(30),primary_key=True,nullable=False)
    type=Column(String(20),nullable=True)
    level=Column(String(20),nullable=True)
    location=Column(String(100),nullable=True)
    speed=Column(Integer,nullable=True)
    source = Column(String(500), nullable=False)
    indate=Column(DateTime,nullable=False)

    def __init__(self,ip_port,source,type=None,level=None,location=None,speed=None):
        self.ip_port=ip_port
        self.type=type
        self.level=level
        self.location=location
        self.speed=speed
        self.source=source
        self.indate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
