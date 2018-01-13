# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import Column,  String, Integer, VARCHAR,ForeignKey, Float
from MyDbInfo import engine,Base,Session_class
import uuid
def gen_id():
    return uuid.uuid4().hex
class Article(Base):
    def __init__(self, title, keywords, digest):
        self.title=title
        self.keywords=keywords
        self.digest=digest
    def __repr__(self):
        return "<Article(id='%s',title='%s',  keywords='%s')>" % (self.id,self.title, self.keywords)
    __tablename__ = 'zhhz_notice_content'
    id = Column("id",VARCHAR(32),default=gen_id,primary_key = True)
    title = Column("notic_title",VARCHAR(100))
    keywords = Column("notic_keywords",VARCHAR(100))
    digest = Column("notic_digest",VARCHAR(1000))
    def save(self):

        # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
        session = Session_class()  # 生成session实例，相当于游标
        article=session.add(self)
        session.commit() #现此才统一提交，创建数据
        print article

