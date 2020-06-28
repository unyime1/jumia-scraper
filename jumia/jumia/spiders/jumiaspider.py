# -*- coding: utf-8 -*-
import scrapy
from ..items import JumiaItem


class JumiaSpider(scrapy.Spider):
    name = 'jumia'
    page_number = 2
    start_urls = [
        'https://www.jumia.com.ng/mobile-phones/samsung/?page=1'
    ]


    def parse(self, response):
        items = JumiaItem()

        containers = response.css('.info')

        for container in containers:
            product_name = container.css('.name::text').extract()
            product_price = container.css('.prc::text').extract() 
            

            items['product_name'] = product_name
            items['product_price'] = product_price
            

            yield items

        next_page = 'https://www.jumia.com.ng/mobile-phones/samsung/?page=' + str(JumiaSpider.page_number) + '/'

        if JumiaSpider.page_number < 17:   #total number of pages to be crawled
            JumiaSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
