import scrapy
from scrapy.utils.response import open_in_browser




class QuotesSpider(scrapy.Spider):
    name = 'pags'
    start_urls = [
        'https://www.google.com/search?q=turismo+minas+gerais&rlz=1C1GCEA_enBR927BR927&oq=turismo+minas+&aqs=chrome.1.69i57j69i59j0l6.5430j1j15&sourceid=chrome&ie=UTF-8',
    ]
    contar = int(0)
 
    def parse(self, response):
        #open_in_browser(response)
        
        c = response.css('.kCrYT a::attr(href)').getall()
        for quote in c:
            yield {
                'link': quote
              
            }

        next_page = response.css('#main > footer > div:nth-child(1) > div > div > a::attr(href)').get()
        if next_page is not None:
            self.contar += 1
            if self.contar < 6:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)