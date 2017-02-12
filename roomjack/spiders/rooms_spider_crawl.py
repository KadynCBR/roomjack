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
from scrapy.linkextractors import LinkExtractor

# this is the actual spider
class MySpider(CrawlSpider):
    # Name the spider, you'll use this to call it for initialization.
    name = ""
    # Since you're automating traversal, set an allowable domain so
    # your crawspider doesn't feel the need to break off the website.
    allowed_domains = [""]
    # Starting points for your spider to crawl from.
    start_urls = (
        "",
    )


    # This is the function that will run on every url response in the
    # the crawlSpider's 'path'.
    def parse_page(self, response):
        pass
