# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CochescomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    descripcion = scrapy.Field()
    modelo = scrapy.Field()
    provincia = scrapy.Field()

    precio = scrapy.Field()
    anyo = scrapy.Field()
    potencia = scrapy.Field()
    kilometros = scrapy.Field()
    combustible = scrapy.Field()
    puertas = scrapy.Field()
    cambio = scrapy.Field()
    emisiones = scrapy.Field()
    vendedor = scrapy.Field()
    garantia = scrapy.Field()
    color_ext = scrapy.Field()

    maletero = scrapy.Field()
    longitud = scrapy.Field()
    altura = scrapy.Field()
    anchura = scrapy.Field()
    puertas = scrapy.Field()
    plazas = scrapy.Field()
    deposito = scrapy.Field()
    peso = scrapy.Field()
    peso_max = scrapy.Field()
    carroceria = scrapy.Field()

    vel_maxima = scrapy.Field()
    c_mixto = scrapy.Field()
    c_urbano = scrapy.Field()
    c_extraurbano = scrapy.Field()
    aceleracion = scrapy.Field()
    autonomia = scrapy.Field()
    emision = scrapy.Field()

    potencia = scrapy.Field()
    cilindrada = scrapy.Field()
    cilindros = scrapy.Field()
    transmision = scrapy.Field()
    par_maximo = scrapy.Field()
    marchas = scrapy.Field()
    traccion = scrapy.Field()


    pass
