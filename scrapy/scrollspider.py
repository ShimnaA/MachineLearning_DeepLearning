import json
import scrapy


class ScrollspiderSpider(scrapy.Spider):
    name = 'scrollspider'
    
    base_url = 'http://quotes.toscrape.com/api/quotes?page=%d'
    start_urls = [base_url % 1]

    def parse(self, response):
        json_data = json.loads(response.text)
        for cell in json_data['quotes']:
            item_data =  { 
                'author name': cell['author']['name'],
                'text': cell['text'],
                'tags': cell['tags']}
            yield item_data   

        if json_data['has_next']:
            print("shim has next *******************************")
            yield scrapy.Request(self.base_url % (int(json_data['page']) + 1))



