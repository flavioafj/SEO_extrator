import scrapy
from scrapy.utils.response import open_in_browser




class QuotesSpider(scrapy.Spider):
    name = 'inputs'
    start_urls = [
        'http://agenciaminas.mg.gov.br/contato',
        'http://www.agenciaminas.mg.gov.br/contato',
        'http://www.descubraminas.com.br/Portal/Contato.aspx',
        'https://apureguria.com/contato/',
        'https://www.tzviagens.com.br/c/758/Contato',
        'https://bodacidade.com.br/conteudo/4/fale-com-o-b-o',
        'https://casalnomade.com/contato/',
        'https://chicaslokas.com.br/contato/',
        'https://foradazonadeconforto.com/contato/',
        'https://guiaviajarmelhor.com.br/contato/',
        'https://magazine.trivago.com.br/contact',
        'https://minasgeraistur.com.br/contato/',
        'https://passageirodeprimeira.com/contato/',
        'https://reservecar.com.br/blog/contact/',
        'https://serrasverdes.com.br/contato/',
        'https://igcorp.octadesk.com/kb/',
        'https://viagemeturismo.abril.com.br/fale-conosco/',
        'https://viajandobem.com.br/contato/',
        'https://viajeiros.com/contato/',
        'https://visiteminasgerais.com.br/contato/',
        'https://vounomundo.com.br/fale-conosco/',
        'https://www.aeroportosdomundo.com/consultas.php',
        'https://www.bolsadeviagem.com.br/pocos-de-caldas/',
        'https://www.carpemundi.com.br/contato/',
        'https://www.casablancaturismo.com.br/contato/',
        'https://www.feriasbrasil.com.br/site/contato.cfm',
        'https://www.guiadasemana.com.br/contato',
        'https://www.itatiaia.com.br/contato',
        'https://www.mg.gov.br/conteudo/atendimento/fale-conosco',
        'https://www.minasgerais.com.br/pt/fale-conosco',
        'https://www.obomdeviajar.com.br/contato/',
        'https://www.proximatrip.com.br/contatopublicidade/',
        'https://www.segueviagem.com.br/fale-com-o-grupo-trend/',
        'https://www.topensandoemviajar.com/sobre',
        'https://www.viagenscinematograficas.com.br/contato',
        'https://www.viajali.com.br/contato/'

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
                'site': response.url,
                'campos': c,
                'texto': d
              
        }

      