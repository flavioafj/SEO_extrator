import scrapy
from scrapy.utils.response import open_in_browser




class QuotesSpider(scrapy.Spider):
    name = 'pags'
    start_urls = [
        'https://www.google.com/search?rlz=1C1GCEA_enBR927BR927&sxsrf=ALeKk02TLugZ_wFdtMJpNrpBG2lxcKb6nw%3A1612993140132&ei=dFIkYKfXB96o5OUP-dOrMA&q=Minas+gerais+f%C3%A9rias&oq=Minas+gerais+f%C3%A9rias&gs_lcp=CgZwc3ktYWIQAzIGCAAQFhAeMgYIABAWEB46BAgjECc6CAgAEMcBEK8BOgIIADoICAAQsQMQgwE6CwgAELEDEMcBEKMCOgUIABCxAzoECC4QQzoECAAQQzoFCC4QsQM6BwguELEDEEM6CwgAELEDEMcBEK8BOgIILjoECC4QCjoKCC4QsQMQChCTAjoHCAAQsQMQCjoECAAQCjoHCCMQsQIQJzoHCC4QsQMQCjoKCAAQxwEQrwEQCjoCCCZQwKcBWPvbAWC55QFoBXACeACAAekBiAHwIJIBBjAuMjAuNZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwin4ZHZo-DuAhVeFLkGHfnpCgYQ4dUDCA0&uact=5'
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
            if self.contar < 200:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)