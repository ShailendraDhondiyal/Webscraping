# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YahoofinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    symbol = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    perc_change = scrapy.Field()
    volume = scrapy.Field()
    volume_3_mth_avg = scrapy.Field()
    market_cap = scrapy.Field()
    pe_ratio = scrapy.Field()
    beta_3y_mthly = scrapy.Field()
    one_yr_target_est = scrapy.Field()
