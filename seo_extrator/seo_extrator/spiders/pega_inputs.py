import scrapy
from scrapy.utils.response import open_in_browser




class QuotesSpider(scrapy.Spider):
    name = 'inputs'
    start_urls = [
        'https://casalnomade.com/contato/'
    ]
    contar = int(0)
 
    def parse(self, response):
        #open_in_browser(response)
        
        c = response.css('form input').getall()
        d = response.css('textarea').get()
        """for quote in c:
            yield {
                'link': quote
              
            }"""
        yield {
                'campos': c,
                'texto': d
              
        }

      