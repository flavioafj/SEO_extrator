import scrapy
import csv
from selenium import webdriver
import pdb
from scrapy.linkextractors import LinkExtractor

class AngularSpider(scrapy.Spider):
    name = 'angular_spider'
    start_urls = [
        'https://magazine.trivago.com.br/lugares-para-viajar-minas-gerais/'
        
    ]    
    
    link_extractor = LinkExtractor()
    
    # Initalize the webdriver    
    def __init__(self):
        self.driver = webdriver.Chrome()

    
    # Parse through each Start URLs
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)    
    

   # Parse function: Scrape the webpage and store it
    def parse(self, response):
        self.driver.get(response.url)
        
        #breakpoint()
        links = self.driver.find_elements_by_css_selector('a')
        for ligacao in links:
            print(ligacao.text + "\n")