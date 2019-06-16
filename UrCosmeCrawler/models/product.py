# coding=utf-8
# 建立資料表欄位
from UrCosmeCrawler.settings import Base
from sqlalchemy import Column, Integer, String, DateTime
import json


class Product(Base):
    __tablename__ = 'product'
    # 設定 primary_key
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    brand_id = Column(Integer)
    category_depth_1_tag_id = Column(Integer)
    category_depth_2_tag_id = Column(Integer)
    category_depth_3_tag_id = Column(Integer)
    series_id = Column(Integer)
    price = Column(String(100))
    volume = Column(String(100))
    release_date = Column(DateTime)

    def __init__(self, id, name, brand_id, category_depth_1_tag_id, category_depth_2_tag_id, category_depth_3_tag_id,
                 series_id, price, volume, release_date
                 ):
        self.id = id
        self.name = name
        self.brand_id = brand_id
        self.category_depth_1_tag_id = category_depth_1_tag_id
        self.category_depth_2_tag_id = category_depth_2_tag_id
        self.category_depth_3_tag_id = category_depth_3_tag_id
        self.series_id = series_id
        self.price = price
        self.volume = volume
        self.release_date = release_date

    def __repr__(self):
        return json.dumps(self)
