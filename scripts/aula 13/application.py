#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:01:17 2022

@author: cafe
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return f"Hello, {name}"
            
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
