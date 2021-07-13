# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:21:54 2021

@author: Administrator
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
     app.run()