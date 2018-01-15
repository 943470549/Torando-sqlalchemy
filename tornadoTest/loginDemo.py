# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.escape
import os
from jinja2 import FileSystemLoader,Environment
import sys
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class BaseHandler(tornado.web.RequestHandler):
    _path_to_env = {}
    def get_current_user(self):
        return self.get_secure_cookie("user")
    def get_template_path(self):
        return os.path.join(os.path.dirname(__file__), "template/")
    def create_template_loader(self, template_path):
        """ 根据template_path创建相对应的Jinja2 Environment """
        temp_path = template_path
        if isinstance(template_path, (list, tuple)):
            temp_path = template_path[0]
        env = BaseHandler._path_to_env.get(temp_path)
        if not env:
            _loader = FileSystemLoader(template_path)
            env = Environment(loader = _loader)
            BaseHandler._path_to_env[temp_path] = env
        return env
    def render_string(self, template_name, **kwargs):
        """ 使用Jinja2模板引擎 """
        env = self.create_template_loader(self.get_template_path())
        t = env.get_template(template_name)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return t.render(**namespace)
class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # if not self.current_user:
        #     self.redirect("/login")
        #     return
        items=["天","b"]
        name = tornado.escape.xhtml_escape(self.current_user)
        self.finish(self.render_string("main.html",title="ceshi",name=name,items=items))
        # self.render(self.get_template_path()+"main.html",title="ceshi",name=name,items=items)
class LoginHandler(BaseHandler):
    def get(self):
        self.finish(self.render_string("login.html"))
        # self.render(self.get_template_path()+"login.html")
    def post(self, *args, **kwargs):
        self.set_secure_cookie("user",self.get_argument("name"))
        self.redirect("/")
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True
}
application2 = tornado.web.Application([
    (r'/',MainHandler),
    (r'/login',LoginHandler),
    (r"/(apple-touch-icon\.jpg)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
],**settings)
if __name__ == "__main__":
    application2.listen(7001)
    tornado.ioloop.IOLoop.instance().start()