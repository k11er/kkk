import scrapy

class ToScrapeCSSSpider(scrapy.Spider):

    name = "csdnASK"

    start_urls = [
        'http://ask.csdn.net/',
    ]

    def parse(self,response):
        for times in response.xpath('//div[@class="questions_detail_con"]'):
            yield {
                'date': times.xpath('./div[@class="q_time"]/span/text()').extract(),
                'tag0': times.xpath('./div[@class="tags"]/a[0]/text()').extract(),
                'tag1': times.xpath('./div[@class="tags"]/a[1]/text()').extract(),
                'tag2': times.xpath('./div[@class="tags"]/a[2]/text()').extract(),
                'tag3': times.xpath('./div[@class="tags"]/a[3]/text()').extract(),
                'tag4': times.xpath('./div[@class="tags"]/a[4]/text()').extract(),
            }

        next_page = response.xpath('//div[@class="csdn-pagination hide-set"]/span/a[last()-1]/text()').extract()
        print(next_page[0])
        if next_page[0] == '下一页':
            next_page_href = response.xpath('//div[@class="csdn-pagination hide-set"]/span/a[last()-1]/@href').extract()[0]
            next_page_href= 'http://ask.csdn.net/'+next_page_href
            yield scrapy.Request(url=next_page_href,callback=self.parse)
