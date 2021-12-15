import scrapy
from scrapy import item
from scrapy.http import Request
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com'] 

    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()

        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        # yield {
        #     'H1 Tags': h1_tag,
        #     'Tags': tags
        # }
        # quotes = response.xpath('//*[@class="quote"]')
        # for quote in quotes:
        #     text = quote.xpath(
        #         './/*[@class="text"]/text()'
        #     ).extract_first()

        #     author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()

        #     tags = quote.xpath('.//*[@class="tag"]/text()').extract()

        #     yield {
        #         'Text': text,
        #         'Author': author,
        #         'Tags': tags
        #     }

        # next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        # yield Request(absolute_next_page_url, callback=self.parse)


        l = ItemLoader(item=QuotesSpiderItem(), response=response)
        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()