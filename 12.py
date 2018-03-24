
以前区分“乡下人”和“城里人”是根据户口来区分的，但国家将要取消农村户口了，户籍制度改革后统一登记，农村户口和城镇户口都登记为“居民户口”，使农民朋友们和城市居民享有同等的社会保障。
import sys


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


