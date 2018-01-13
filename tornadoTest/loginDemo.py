# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.escape
import os

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")
    def get_template_path(self):
        return os.path.join(os.path.dirname(__file__), "template/")
class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # if not self.current_user:
        #     self.redirect("/login")
        #     return
        items=["a","b"]
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render(self.get_template_path()+"main.html",title="ceshi",name=name,items=items)
class LoginHandler(BaseHandler):
    def get(self):
        self.render(self.get_template_path()+"login.html")
    def post(self, *args, **kwargs):
        self.set_secure_cookie("user",self.get_argument("name"))
        self.redirect("/")
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
}
application2 = tornado.web.Application([
    (r'/',MainHandler),
    (r'/login',LoginHandler),
    (r"/(apple-touch-icon\.jpg)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
],**settings)
if __name__ == "__main__":
    application2.listen(7001)
    tornado.ioloop.IOLoop.instance().start()