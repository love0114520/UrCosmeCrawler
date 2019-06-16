# coding=utf-8
# 建立資料表欄位
from UrCosmeCrawler.settings import Base
from sqlalchemy import Column, Integer, String
import json


class Tag(Base):
    __tablename__ = 'tag'
    # 設定 primary_key
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return json.dumps(self)
