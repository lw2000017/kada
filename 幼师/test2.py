#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-19 19:06:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import sys
import importlib
importlib.reload(sys)


from flask import Flask
import flask_restful


app = Flask(__name__)

api	= flask_restful.Api(app)


class HelloWorld(flask_restful.Resource):
	def get(self):
		return {"hello":"world"}


api.add_resource(HelloWorld,'/')


if __name__ == '__main__':
	app.run(host = '0.0.0.0')