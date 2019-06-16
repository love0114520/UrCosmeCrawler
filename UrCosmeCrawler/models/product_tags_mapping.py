# coding=utf-8
# 建立資料表欄位
from UrCosmeCrawler.settings import Base
from sqlalchemy import Column, Integer
import json


class ProductTagsMapping(Base):
    __tablename__ = 'product_tags_mapping'
    # 設定 primary_key
    product_id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, primary_key=True)

    def __init__(self, product_id, tag_id):
        self.product_id = product_id
        self.tag_id = tag_id

    def __repr__(self):
        return json.dumps(self)
