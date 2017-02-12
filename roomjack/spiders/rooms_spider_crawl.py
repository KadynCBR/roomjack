#!/user/bin/python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# rooms_spider.py
#------------------------------------------------------------------------------
# Spider for scraping rooms and apartments off of craigslist.com.
#------------------------------------------------------------------------------
# Author: Kadyn Martinez (kadyn_martinez@hotmail.com)
#------------------------------------------------------------------------------
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import linkextractors

# this is the actual spider
class RoomSpider(CrawlSpider):
    # Name the spider, you'll use this to call it for initialization.
    name = "roomcrawl"
    # Since you're automating traversal, set an allowable domain so
    # your crawspider doesn't feel the need to break off the website.
    start_urls = (
    "sfbay.craigslist.org",
    )
    # This is the function that will run on every url response in the
    # the spider crawls
    def parse_page(self, response):
