# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LznetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    district = scrapy.Field()   #上海区名称
    district_link = scrapy.Field()  #上海各区的链接
    district_title = scrapy.Field()  # 链接的title
    district_getdate = scrapy.Field()  # 链接的title
    # town = scrapy.Field()         #每个区的镇(区域)的名称
    # town_link = scrapy.Field()    #每个区的镇(区域)的链接
    # town_totalpage = scrapy.Field()   #每个区的镇(区域)的房子的总页数

