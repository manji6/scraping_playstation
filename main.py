import os
from flask import Flask, jsonify
from scraper import Scraper


app = Flask(__name__)
scraper = Scraper()


@app.route("/")
def store_playstation():
    return jsonify(scraper.store_playstation("https://store.playstation.com/ja-jp/category/1b6c3e7d-4445-4cef-a046-efd94a1085b7/"))



if __name__ == "__main__":
    app.run(port=8001,debug=True)