import scrapy
from ..items import CroncheckItem

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['www.accuweather.com']
    start_urls = ['https://www.accuweather.com/en/pk/pakistan-weather']

    def parse(self, response):
        items = CroncheckItem()
        # id = 0
        n=0
        while n < 20:
            city = response.css('.no-wrap::text')[n].extract()
            curr_temp  = response.css('.temp::text')[n].extract()
            # id += 1
            n += 1
            # items['id'] = id
            items['city'] = city
            items['curr_temp'] = curr_temp
            yield items
