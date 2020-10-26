import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import CochescomItem

class CochescomSpider(CrawlSpider):
    name = 'cochescom'
    allowed_domains = ['coches.com']
    start_urls = ['https://www.coches.com/coches-segunda-mano/coches-ocasion.htm']

    rules = (
        # Paginacion
        Rule(LinkExtractor(
            allow=r'page='
        ), follow=True),

        # Detalle de coches
        Rule(LinkExtractor(
            allow='/ocasion-'
        ), follow=True, callback='parse_coche'
        ),
    )

    def parse_coche(self, response):
        items = CochescomItem()

        items["descripcion"] = response.xpath('//*[@id="indexCardVehicleDescription"]/div/div[1]/text()').extract_first().strip()
        items["modelo"] = ' '.join(response.xpath('//*[@id="trackingIndexCardPromotion"]/div[1]/div[1]/h1/strong/text()').extract_first().strip().split())
        items["provincia"] = response.xpath('//*[@id="trackingIndexCardPromotion"]/div[1]/div[1]/div/div/text()').extract_first().strip()

        for element in response.xpath('//*[@id="indexCardPpal"]/div[1]/div[4]/div[1]/div'):
            # print(element.css('div.index-card__technical-data-label::text').extract_first())
            # print(element.css('div.index-card__technical-data-info::text').extract_first())
            nombre = element.css('div.index-card__technical-data-label::text').extract_first().strip()
            valor = element.css('div.index-card__technical-data-info::text').extract_first().strip()
            if nombre == "Precio":
                items["precio"] = valor
            elif nombre == "Año":
                items["anyo"] = valor
            elif nombre == "Potencia":
                items["potencia"] = valor
            elif nombre == "Kilómetros":
                items["kilometros"] = valor
            elif nombre == "Combustible":
                items["combustible"] = valor
            elif nombre == "Puertas":
                items["puertas"] = valor
            elif nombre == "Cambio":
                items["cambio"] = valor
            elif nombre == "Emisiones":
                items["emisiones"] = valor
            elif nombre == "Vendedor":
                items["vendedor"] = valor
            elif nombre == "Garantía":
                items["garantia"] = valor
            elif nombre == "Color exterior":
                items["color_ext"] = valor


        for element in response.xpath('//*[@id="indexCardTechnicalData"]/div[1]/div/div'):
            # print(element.css('div.index-card__technical-data-label::text').extract_first())
            # print(element.css('div.index-card__technical-data-info::text').extract_first())
            nombre = element.css('div.index-card__technical-data-label::text').extract_first().strip()
            valor = element.css('div.index-card__technical-data-info::text').extract_first().strip()
            if nombre == "Maletero":
                items["maletero"] = valor
            elif nombre == "Longitud":
                items["longitud"] = valor
            elif nombre == "Altura":
                items["altura"] = valor
            elif nombre == "Anchura":
                items["anchura"] = valor
            elif nombre == "Puertas":
                items["puertas"] = valor
            elif nombre == "Plazas":
                items["plazas"] = valor
            elif nombre == "Depósito":
                items["deposito"] = valor
            elif nombre == "Peso":
                items["peso"] = valor
            elif nombre == "Peso Max.":
                items["peso_max"] = valor
            elif nombre == "Garantía":
                items["garantia"] = valor
            elif nombre == "Carrocería":
                items["carroceria"] = valor

        for element in response.xpath('//*[@id="indexCardTechnicalData"]/div[2]/div/div'):
            # print(element.css('div.index-card__technical-data-label::text').extract_first())
            # print(element.css('div.index-card__technical-data-info::text').extract_first())
            nombre = element.css('div.index-card__technical-data-label::text').extract_first().strip()
            valor = element.css('div.index-card__technical-data-info::text').extract_first().strip()
            if nombre == "Vel. máxima":
                items["vel_maxima"] = valor
            elif nombre == "C. mixto":
                items["c_mixto"] = valor
            elif nombre == "C. urbano":
                items["c_urbano"] = valor
            elif nombre == "Extraurbano":
                items["c_extraurbano"] = valor
            elif nombre == "0-100 km/h":
                items["aceleracion"] = valor
            elif nombre == "Autonomía":
                items["autonomia"] = valor
            elif nombre == "Emisión CO2":
                items["emision"] = valor


        for element in response.xpath('//*[@id="indexCardTechnicalData"]/div[3]/div/div'):
            # print(element.css('div.index-card__technical-data-label::text').extract_first())
            # print(element.css('div.index-card__technical-data-info::text').extract_first())
            nombre = element.css('div.index-card__technical-data-label::text').extract_first().strip()
            valor = element.css('div.index-card__technical-data-info::text').extract_first().strip()
            if nombre == "Potencia":
                items["potencia"] = valor
            elif nombre == "Cilindrada":
                items["cilindrada"] = valor
            elif nombre == "Cilindros":
                items["cilindros"] = valor
            elif nombre == "Transmisión":
                items["transmision"] = valor
            elif nombre == "Par máximo":
                items["par_maximo"] = valor
            elif nombre == "Marchas":
                items["marchas"] = valor
            elif nombre == "Tracción":
                items["traccion"] = valor

        return items
