import tornado.ioloop
import tornado.web

class mainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello %s " %self.request.arguments )
        self.write("hello %s " %self.request.files  )
        self.write("hello %s " %self.request.headers  )
        self.redirect('/aa', permanent=True)
class aaHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello aa ")


application=tornado.web.Application([
    (r"/",mainHandler),
    (r"/aa",aaHandler),
    (r"/test",tornado.web.RedirectHandler,dict(url="/")),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()