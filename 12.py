
from tornado import  web,ioloop,httpserver


#具体的页面
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #self.write('徐开峰')
        self.render('index.html')

class CreatDiaryHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #self.write('徐开峰')
        self.render('create.html')



#分机号
application = web.Application ([
    (r"/", MainPageHandler),
    (r"/create", CreatDiaryHandler),
])
#前台总机
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8089)
    ioloop.IOLoop.current().start()
