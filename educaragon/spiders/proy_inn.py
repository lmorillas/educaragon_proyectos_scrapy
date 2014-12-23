# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from educaragon.items import EducaragonItem


'''
Inicio : http://www.educaragon.org/impresos/formato9/formato9_list.asp?idTabla=45


'''


class ProyInnSpider(scrapy.Spider):
    name = "proy_inn"
    allowed_domains = ["educaragon.org"]
    start_urls = (
        'http://www.educaragon.org/impresos/formato9/formato9_list.asp?idTabla=45',
    )

    def parse(self, response):
        # tope: 35 : http://www.educaragon.org/impresos/formato9/formato9_list.asp?idTabla=45&pag=35
        MAX = 35
        for x in range(1, MAX+1):
            yield scrapy.Request(self. start_urls[0]+"&pag={}".format(x), callback = self.parse_lista)

    def parse_lista(self, response):
        sel = Selector(response)
        for proyecto in sel.xpath('//a/@href[contains(., "formato9_ficha") ]'):
                yield scrapy.Request("http://www.educaragon.org/impresos/formato9/{}".format(proyecto.extract()),
                    callback = self.parse_proyecto)

    def parse_proyecto(self, response):
        sel = Selector(response)
        url = response.url
        titulo = sel.xpath(u'//td[contains(b, "Título")]//font/text()').extract()
        coord = sel.xpath('//td[contains(b, "Autor")]/text()').extract()
        centro = sel.xpath('//td[contains(b, "Centro")]/text()').extract()
        curso = sel.xpath('//td[contains(b, "Curso")]/text()').extract()
        temas = sel.xpath(u'//td[contains(b/font, "Temas")]/a/text()').extract()
        item = EducaragonItem()
        item['titulo'] = titulo
        item['coord'] = coord
        item['centro'] = centro
        item['curso'] = curso
        item['temas'] = temas
        item['url'] = url
        yield item
