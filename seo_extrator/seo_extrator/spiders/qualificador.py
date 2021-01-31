import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.linkextractors import LinkExtractor
import re
import pdb
import datetime
from scrapy import Request
from scrapy_selenium import SeleniumRequest
from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS='--headless'  # '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

class QuotesSpider(scrapy.Spider):
    name = 'inde'
    start_urls = [
        'http://www.descubraminas.com.br/turismo/circuito.aspx',
        'https://guiaviajarmelhor.com.br/8-lugares-imperdiveis-para-conhecer-em-minas-gerais/',
        'https://magazine.trivago.com.br/lugares-para-viajar-minas-gerais/',
        'https://turismo.ig.com.br/2020-11-24/conheca-destinos-perfeitos-para-viajar-entre-sao-paulo-e-minas-gerais.html',
        'https://turismodeminas.com.br/',
        'https://turismodeminas.com.br/dicas/roteiros-de-carro-por-minas-gerais/',
        'https://viagemeturismo.abril.com.br/estados/minas-gerais/',
        'https://viagemeturismo.abril.com.br/materias/refugios-no-interior-de-minas-gerais-que-vao-te-deixar-zen/',
        'https://www.em.com.br/app/noticia/gerais/2020/08/20/interna_gerais,1177704/turismo-em-minas-se-adapta-ao-novo-normal-imposto-pelo-coronavirus.shtml',
        'https://www.instagram.com/turismodeminas/',
        'https://www.minasgerais.com.br/',
        'https://www.minasgerais.com.br/pt/blog/artigo/relatos-de-viagens-dicas-incriveis-do-que-conhecer-em-minas',
        'https://www.minasimperador.com.br/',
        'https://www.observatorioturismo.mg.gov.br/',
        'https://www.passagenspromo.com.br/blog/cidades-turisticas-de-minas-gerais/',
        'https://www.passagenspromo.com.br/blog/turismo-em-minas-gerais/',
        'https://www.skyscanner.com.br/noticias/minas-gerais-o-que-fazer-e-cidades-imperdiveis-para-visitar',
        'https://www.tripadvisor.com.br/Attractions-g303370-Activities-State_of_Minas_Gerais.html',
        'https://www.viajali.com.br/turismo-minas-gerais-cenarios/'

    ]
    
    link_extractor = LinkExtractor()
    
   

    with open("palavras.txt", "r")as f:
        palavras = str(f.read())
    f.close()
    lista_de_palavras = palavras.split(", ")
   
    titulo = str()
    contato2 = list()
    valor = float(1/len(lista_de_palavras))

    nota = float(0)
    def parse(self, response):
        self.nota = 0
        vai_render = bool(True)
        self.titulo = str()
        self.titulo = response.css('h1::text').get()
        
        
     
        if response.url == 'https://magazine.trivago.com.br/lugares-para-viajar-minas-gerais/':
            yield SeleniumRequest(url=response.url, callback=self.parse2)
            open_in_browser(response)
            breakpoint()
            
        

        #open_in_browser(response)
        for palavra in self.lista_de_palavras:
            if palavra in response.text.lower():
                self.nota += self.valor
         

            
        for link in self.link_extractor.extract_links(response):
           
                               
            if "contato" in link.text.lower() or "fale conosco" in link.text.lower() or "contact" in link.text.lower():
                vai_render = bool(False)
                
            
                yield scrapy.Request(link.url, callback=self.contato, cb_kwargs=dict(titulo2=self.titulo, nota2=self.valor, original_url=response.url))
               
                break
        
        
        if vai_render == True:    
            yield{
            "dominio": response.url,
            "nota": self.nota,
            "titulo": self.titulo,
            "contato": "Não encontrado"
            
            }
                
        
    
    def contato(self, response, titulo2, nota2, original_url):
        texto = response.text
        
        dicio = re.findall(r'\S+@\S+', texto)
        for um in dicio:
            self.contato2 += ", "
        #self.contato2 = re.findall(r'([^@|\s]+@[^@]+\.[^@|\s]+)', texto)
        if len(self.contato2) == 0:
            #self.contato2 = response.css('input').getall()
            self.contato2 = response.url
        
        """if original_url == 'https://magazine.trivago.com.br/lugares-para-viajar-minas-gerais/':
            breakpoint()"""
        
        yield{
            "dominio": original_url,
            "nota": nota2,
            "titulo": titulo2,
            "contato": self.contato2
            
        }
       
    def parse2(self, response):
        print("contato" in response.text.lower())
        breakpoint()
        

       