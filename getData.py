import scrapy

class Tecmundo (scrapy.Spider):
    name = 'tecmundo'
    start_urls = ['https://www.tecmundo.com.br/novidades']

    def parse(self, response):
        title = response.css('h3 a::text').getall()
        url = response.css('h3 a::attr(href)').getall()
        yield {
            "title":title,
            "url":url
            }
