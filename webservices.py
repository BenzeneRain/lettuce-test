#!/usr/bin/env python
import tornado
import tornado.web
import tornado.ioloop


class HelloHandler(tornado.web.RequestHandler):	
	def get(self):
		self.write("Hello, world!")


application = tornado.web.Application([
		(r"/", HelloHandler),
		])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
