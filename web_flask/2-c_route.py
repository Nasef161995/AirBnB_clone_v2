#!/usr/bin/python3
"""Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_C(text):
    part = text.split("_")
    return f"C {part[0]} {part[1]}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
