import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.linkextractors import LinkExtractor
import re
import pdb
import datetime
from scrapy import Request
from scrapy_selenium import SeleniumRequest
from shutil import which



class QuotesSpider(scrapy.Spider):
    name = 'inde'
    start_urls = [
        'https://www.tripadvisor.com.br/Tourism-g303370-State_of_Minas_Gerais-Vacations.html',
        'https://www.tripadvisor.com.br/Vacation_Packages-g303370-State_of_Minas_Gerais-Vacations.html',
        'https://www.tripadvisor.com.br/ShowForum-g303370-i4771-State_of_Minas_Gerais.html',
        'https://www.tripadvisor.com.br/Hotels-g303370-State_of_Minas_Gerais-Hotels.html',
        'https://www.tripadvisor.com.br/Attractions-g303370-Activities-State_of_Minas_Gerais.html',
        'https://www.feriasbrasil.com.br/mg/',
        'https://www.minasgerais.com.br/pt/blog/artigo/4-destinos-para-suas-ferias',
        'https://magazine.trivago.com.br/lugares-para-viajar-minas-gerais/',
        'https://turismodeminas.com.br/dicas/roteiros-de-carro-por-minas-gerais/',
        'https://clubdeferias.tur.br/locais/destinos/Minas%252BGerais',
        'https://www.booking.com/holiday-homes/region/br/minas-gerais.pt-pt.html',
        'https://www.expedia.com.br/Minas-Gerais-Casas-De-Ferias.d6052632-aaCasasDeFerias.Guia-Viagens-Hospedagem',
        'https://www.portaldoservidor.mg.gov.br/index.php/acesso-a-informacao/direitos-do-servidor/ferias/ferias-regulamentares',
        'https://www.portaldoservidor.mg.gov.br/index.php/acesso-a-informacao/direitos-do-servidor/ferias/concessao-de-ferias-premio',
        'https://muitaviagem.com.br/b/sul-de-minas/',
        'https://catracalivre.com.br/viagem-livre/10-dicas-imperdiveis-para-voce-curtir-as-ferias-em-minas-gerais/',
        'http://www.fazenda.mg.gov.br/servidores/cadastro_beneficios/ferias_regulamentares/',
        'http://www.fazenda.mg.gov.br/servidores/cadastro_beneficios/ferias_regulamentares/page/',
        'http://agenciaminas.mg.gov.br/noticia/governo-esclarece-que-pagamento-do-um-terco-de-ferias-esta-regularizado',
        'http://www.agenciaminas.mg.gov.br/noticia/belezas-naturais-de-minas-sao-atrativo-no-periodo-de-ferias',
        'https://g1.globo.com/mg/minas-gerais/noticia/2021/01/18/casos-de-covid-19-em-bh-podem-aumentar-8-vezes-com-viagens-de-ferias-se-nao-houver-isolamento.ghtml',
        'https://www4.tjmg.jus.br/juridico/sf/proc_peca_movimentacao.jsp%3Fid%3D930897%26hash%3D50eb2ba2aee1513e669a73f59ea5d445',
        'https://www.sindpolmg.org.br/governo-de-minas-limita-ferias-premio/',
        'https://www.kayak.com.br/packagetours/minas-gerais'







    ]
    
    custom_settings = {
        'SELENIUM_DRIVER_NAME':'chrome',
        'SELENIUM_DRIVER_EXECUTABLE_PATH' : 'C:\\Users\\Cliente\\webdriver\\chromedriver.exe',
        'SELENIUM_DRIVER_ARGUMENTS':['--headless'],  # '--headless' if using chrome instead of firefox
        'DOWNLOADER_MIDDLEWARES' :{
            'scrapy_selenium.SeleniumMiddleware': 800
        }
    }
    
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
        self.contato2 = list()
        
        
     
            
            
        

        #open_in_browser(response)
        for palavra in self.lista_de_palavras:
            if palavra in response.text.lower():
                self.nota += self.valor
         

            
        for link in self.link_extractor.extract_links(response):
           
                               
            if "contato" in link.text.lower() or "fale conosco" in link.text.lower() or "contact" in link.text.lower():
                vai_render = bool(False)
                
            
                yield scrapy.Request(link.url, callback=self.contato, cb_kwargs=dict(titulo2=self.titulo, nota2=self.nota, original_url=response.url))
               
                break
                
        if vai_render == True: 
            yield SeleniumRequest(url=response.url, callback=self.parse2, cb_kwargs=dict(titulo2=self.titulo, nota2=self.nota, original_url=response.url), dont_filter=True, wait_time=10)
            
   
    
    def contato(self, response, titulo2, nota2, original_url):
        texto = response.xpath('//body//text()').getall()
        texto2 = str()
        for fragmento in texto:
            texto2 += fragmento + ", "
        
        #dicio = re.findall(r'\S+@\S+', texto)
        dicio = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', texto2[:-2])
        for um in dicio:
            if len(um)>50:
                dicio.remove(um)

       
        
        #self.contato2 = re.findall(r'([^@|\s]+@[^@]+\.[^@|\s]+)', texto)
        if len(dicio) == 0:
            #self.contato2 = response.css('input').getall()
            self.contato2 = response.url
        else:
            dois = str()
            for um in dicio:
                dois += um + ", "
            self.contato2 = dois[:-2]
        
        """if original_url == 'https://www.minasimperador.com.br/':
            breakpoint()"""
        
        yield{
            "dominio": original_url,
            "nota": nota2,
            "titulo": titulo2,
            "contato": self.contato2
            
        }
       
    def parse2(self, response, titulo2, nota2, original_url):
        vao = bool(True)
        for linke in self.link_extractor.extract_links(response):
            if "contato" in linke.text.lower() or "fale conosco" in linke.text.lower() or "contact" in linke.text.lower():
                vao = bool(False)
                
                yield scrapy.Request(linke.url, callback=self.contato, cb_kwargs=dict(titulo2=titulo2, nota2=nota2, original_url=original_url))
            
            
        if vao == bool(True):    
            yield{
            "dominio": original_url,
            "nota": nota2,
            "titulo": titulo2,
            "contato": "Não encontrado"
            
            }
            
            
        
        

       