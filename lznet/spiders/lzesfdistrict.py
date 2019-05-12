# -*- coding: utf-8 -*-
import scrapy
from lznet.items import LznetItem
from datetime import date


#运行方式一
#在此爬虫目录运行 scrapy crawl
class LzesfdistrictSpider(scrapy.Spider):
    name = 'lzesfdistrict'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['https://sh.lianjia.com/ershoufang/']

    def parse(self, response):

        print self.start_urls[0]

        # pass
        #函数说明
        # string():取到标签下所有的文本（包括子孙标签的文本）
        # text()：取到该标签的文本（不包括子孙标签的文本）
        # extract(): 获取网页标签的内容
        print ("start parse")
        lznet_district = response.xpath('//div[@data-role="ershoufang"]/div/a')
        # print (lznet_district)
        # print type(lznet_district)
        # print len(lznet_district)
        for item in lznet_district:
            item_1 = LznetItem()
            district_link = item.xpath('@href').extract()
            district_title = item.xpath('@title').extract()
            district = item.xpath('text()').extract()
            if district_link:
                item_1['district_link'] = district_link[0]
            else:
                item_1['district_link'] = ''
            if district_title:
                item_1['district_title'] = district_title[0]
            else:
                item_1['district_title'] = ''
            if district:
                item_1['district'] = district[0]
            else:
                item_1['district'] = ''
            itemdate = date.today().strftime("%Y-%m-%d");
            item_1['district_getdate'] = itemdate
            # 将item提交给管道
            yield item_1





