# -*- coding: utf-8 -*-
import time
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from mytestdb import Article,Session_class


class serviceTest():
    executor=ThreadPoolExecutor(10)
    @run_on_executor
    def saveArticle(self,title='', keywords='', digest=''):
        article = Article (title,keywords,digest)
        article.save()
        return article
    @run_on_executor
    def selectTopTen(self):
        session = Session_class()  # 生成session实例，相当于游标
        list=session.query(Article).limit(10)
        return list
    @run_on_executor
    def selectTopOne(self):
        session = Session_class()  # 生成session实例，相当于游标
        list=session.query(Article).first()
        return list
