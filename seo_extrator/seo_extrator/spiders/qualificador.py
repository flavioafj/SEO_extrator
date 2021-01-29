import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.linkextractors import LinkExtractor
import re



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
   
    #valor = float()
    contato2 = list()
    valor = float(1/len(lista_de_palavras))

    nota = float(0)
    def parse(self, response):
        self.nota = 0
        
        #open_in_browser(response)
        for palavra in self.lista_de_palavras:
            if palavra in response.text.lower():
                self.nota += self.valor
         

            
        for link in self.link_extractor.extract_links(response):
            if link.text.lower() == "contato" or link.text.lower() == "fale conosco":
                yield scrapy.Request(link.url, callback=self.contato)
        
        
    
    def contato(self, response):
        texto = response.text
        
        self.contato2 = re.findall(r'\S+@\S+', texto)
        if len(self.contato2) == 0:
            self.contato2 = response.css('input').getall()
        
        yield{
            "dominio": response.url,
            "nota": self.nota,
            "contato": self.contato2
        }
       
        

       