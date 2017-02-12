import scrapy

# this is the actual spider
class RoomSpider(scrapy.Spider):
    # Name the spider, you'll use this to call
    # it for initialization.
    name = "room"

    # This is where you spider starts, you can think of this as initialzing
    # the spider.
    def start_requests(self):
        # these will present the starting points for your crawls.
        urls = [
            'https://sfbay.craigslist.org/search/apa'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # This is the function that will run on every url response in the
    # start_requests function
    def parse(self, response):
    
