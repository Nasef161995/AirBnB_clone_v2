#!/usr/bin/python3
from flask import Flask

hello = Flask(__name__)

@hello.route("/", strict_slashes=False)
def hello_world():
    return "<p>Hello, World!</p>"

@hello.route("/m")
def hello_route():
    return "<p> you are in /. route</p>"

if __name__ == "__main__":
    hello.run(host="0.0.0.0", port=5000)
