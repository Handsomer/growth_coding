#!/usr/bin/evn python
# coding=utf-8

import scrapy
import json

scrapy.optional_features.remove('boto')

class CrawXitaiOfifce(scrapy.Spider):
    name = "eleme"
    location = "望京SOHO"
    start_urls = ("https://www.ele.me/restapi/v2/pois?extras%5B%5D=count&geohash=wx4g0bmjetr7&keyword={}&limit=20&type=nearby".format(location),)
    # start_urls = ("http://blog.csdn.net/dev_csdn/article/details/79415323",)
    def parse(self, response, times=0):
        json_data = json.loads(response.body)
        print(type(json_data))
        elem = json_data[0]
        shop_url = "https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash={}&latitude={}&limit=24&longitude={}&offset=24&terminal=web".format(elem["geohash"],elem["latitude"],elem["longitude"])
        yield scrapy.Request(shop_url, callback=self.parse_shop)
    def parse_shop(self,response,times = 0):
        # with open("/home/sun_pro/code/growth_coding/eleme/shop_msg.log",'w')as fd:
        #     fd.write(response.body)
        "scheme"
        json_data = json.loads(response.body)
        shop_detail = "https://www.ele.me/restapi/shopping/v2/menu?restaurant_id="
        elem = json_data[0]
        print(elem["scheme"])
        target_url  = shop_detail + elem["scheme"].split('=')[1]
        yield scrapy.Request(target_url, callback=self.detail_shop)
        # print(response.body)
    def detail_shop(self,response,times = 0):
        print(response.body)


