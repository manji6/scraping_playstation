# scraping 処理コード
# ---------------------------------------------------
from unicodedata import category
import requests
import bs4
import logging
import re
import json
import pprint
import urllib.parse

class Scraper():
    def store_playstation(self,url):

        # 指定したセールページのデータを取得
        response = requests.get(url)

        # Category ID をURLから取得
        url_parse = urllib.parse.urlparse(url)
        category_id = re.findall('\/category\/(.+?)\/',url_parse.path)[0]


        # 結果をパース
        soup = bs4.BeautifulSoup(response.text,"lxml")
        # parsed_page = soup.select("a[data-track='web:store:product-tile']")
        parsed_script = soup.find_all("script")

        for item in parsed_script:
            if item.get_text().startswith('{"props":'):
                data_products = json.loads(item.get_text())["props"]["apolloState"]


        print(category_id)

        # Product情報配列取り出し
        country_code = "ja-jp"
        offset_info = "0:24"
        items_product_info = data_products["CategoryGrid:" + category_id + ":" + country_code + ":" + offset_info]["products"]
        items = []

        for item in items_product_info:
            item = {
                "title": data_products[item["id"]]["name"],
                "price": data_products[data_products[item["id"]]["price"]["id"]],
                "storeDisplayClassification": data_products[item["id"]]["storeDisplayClassification"]
            }
            items.append(item)

#         # SKU取り出し
#         for item in data_products:
#             print(item)
#             if re.search('^Product:([^\.]+)',item):
# #                pprint.pprint(data_products[item])
#                 # SKU
#                 item_sku = re.findall('^Product:([^\.]+)',item)
#                 print(item_sku)
#                 # items_product_sku.append(item_sku[0])
        
        # for item in items_product_sku:
        #     item = {
        #         "title": data_products[item + country_code]["name"],
        #         "id": data_products[item + country_code]["id"]
        #     }


        # タイトルの抽出
        # for item in parsed_page:
        #     item = {
        #         "title": item.select("span[data-qa$='product-name']")[0].text,
        #         "price": item.select("span[data-qa$='display-price']")[0].text
        #     }
        #     items.append(item)

        pprint.pprint(items)
        
        return items