## items.py
import scrapy


class GameItem(scrapy.Item):
    url = scrapy.Field()
    inning = scrapy.Field()
    description = scrapy.Field()
