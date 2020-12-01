import scrapy


class PaginateSpiderSpider(scrapy.Spider):
    name = 'paginate_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        cells_list = response.css('div.quote')
        for cell in cells_list:
            item_data =  { 
                'author name': cell.css('small.author::text').extract_first(),
                'text': cell.css('span.text::text').extract_first(),
                'tags': cell.css('a.tag::text').extract()}
            yield item_data   

        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page = response.urljoin(next_page_url)
            yield scrapy.Request(next_page, callback=self.parse)

