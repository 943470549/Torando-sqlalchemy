# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker


# 创建实例，并连接test库
engine = create_engine("mysql+pymysql://jpwg:jpwg@172.16.2.202:3306/zhhz_test",
                       encoding='utf-8',convert_unicode=True, #数据库charset
                       pool_size=10,                          #数据库保持连接
                       max_overflow=1000,                     #数据库最大可超连接
                       pool_recycle=60,                       #空闲连接释放
                       echo=False)
# echo=True 显示信息
Base = declarative_base()  # 生成orm基类
Session_class = sessionmaker(bind=engine)  # 实例和engine绑定
print engine


