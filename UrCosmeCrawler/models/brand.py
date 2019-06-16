# coding=utf-8
# 建立資料表欄位
from UrCosmeCrawler.settings import Base
from sqlalchemy import Column, Integer, String
import json


class Brand(Base):
    __tablename__ = 'brand'
    # 設定 primary_key
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    follow_number = Column(Integer)

    def __init__(self, id, name, follow_number):
        self.id = id
        self.name = name
        self.follow_number = follow_number

    def __repr__(self):
        return json.dumps(self)
