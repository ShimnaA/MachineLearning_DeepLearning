import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        return {
		'author name': response.css('small.author::text').extract_first(),
		'text': response.css('span.text::text').extract_first(),
		'tags': response.css('a.tag::text').extract()

	}