# coding=utf-8
# 建立資料表欄位
from UrCosmeCrawler.settings import Base
from sqlalchemy import Column, Integer, String, DateTime, UnicodeText
import json


class Review(Base):
    __tablename__ = 'review'
    # 設定 primary_key
    id = Column(Integer, primary_key=True)
    user_skin = Column(String(256), nullable=False)
    user_age = Column(Integer, nullable=False)
    publish_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=True)
    content = Column(UnicodeText, nullable=False)
    product_id = Column(Integer)

    def __init__(self, id, user_skin, user_age, publish_date, content
                 , product_id
                 , update_date=None):
        self.id = id
        self.user_skin = user_skin
        self.user_age = user_age
        self.publish_date = publish_date
        self.update_date = update_date
        self.content = content
        self.product_id = product_id

    def __repr__(self):
        return json.dumps(self)
