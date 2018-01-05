import scrapy

class ToScrapeCSSSpider(scrapy.Spider):

    name = "csdnASK"

    start_urls = [
        'http://ask.csdn.net/',
    ]

    def parse(self, response):

        for times in response.xpath('//div[@class="questions_detail_con"]'):
            yield {
                'date': times.xpath('./div[@class="q_time"]/span/text()').extract(),
                'tags': times.xpath('./div[@class="tags"]//a/text()').extract(),
            }
