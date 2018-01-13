# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.escape
import tornado.curl_httpclient
import tornado.gen
import time
import json
from  tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
# import imp
# testService = imp.load_source('testService',r'service/testService.py')
from services import *
import sys
from services.mytestdb import Article,Session_class
sum = 0
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return None

class MainHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        http=tornado.curl_httpclient.AsyncHTTPClient()
        http.fetch("http://www.baidu.com",
                   callback=self.on_response)
    def on_response(self, response):
        if response.error:
            print response
        self.write(response.body)
        self.finish()
class SearchHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        url=self.request.uri
        http=tornado.curl_httpclient.AsyncHTTPClient()
        http.fetch("http://www.baidu.com"+url,
                   callback=self.on_response)
    def on_response(self, response):
        if response.error:
            print response
        self.write(response.body)
        self.finish()

class testHandler(BaseHandler):
    executor=ThreadPoolExecutor(50)
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        global sum
        sum+=1
        print ('start:'+str(sum))
        # over = yield testService.serviceTest().saveArticle("11")
        list = yield testService.serviceTest().selectTopTen()
        article = yield testService.serviceTest().selectTopOne()
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # self.write("article %s" %article.title)
        for o in list:
            self.write("article %s" %o.title)
        print('return :'+str(sum))




app=tornado.web.Application([
    (r"/",MainHandler),
    (r"/test",testHandler),
    (r"/[\s\S]*",SearchHandler),
])
app.listen(8888)
tornado.ioloop.IOLoop.instance().start()

