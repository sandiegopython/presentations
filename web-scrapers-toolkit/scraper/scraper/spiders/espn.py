## spiders/espn.py

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scraper.items import GameItem


class EspnSpider(CrawlSpider):
    name = 'espn'
    allowed_domains = ["espn.com", "espn.go.com"]

    # start on the World Series page
    start_urls = ['http://espn.go.com/mlb/playoffs/2014/matchup/_/teams/sfo-kan']
    rules = [Rule(LinkExtractor(allow=['/mlb/playbyplay\?id=\d+']), 'parse_game')]

    def parse_game(self, response):
        game = GameItem()
        game['url'] = response.url
        game['description'] = response.xpath('//div[@class="game-time-location"]/p/text()').extract()
        return game
