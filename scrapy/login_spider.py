import scrapy
from scrapy.http import FormRequest

class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'
    allowed_domains = ['toscrape.com']
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        token = response.css('input[name=csrf_token]::attr(value)').extract_first()
        data = {
            'csrf_token': token,
            'username': 'abc',
            'password': 'abc'
        }
        return scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        for cell in response.css('div.quote'):
            itemdata =  {
                'author name': cell.css('small.author::text').extract_first(),
                'author_url': cell.css('a::attr(href)').extract()[1]}
            yield itemdata   