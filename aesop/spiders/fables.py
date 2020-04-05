# -*- coding: utf-8 -*-
import scrapy

class FablesSpider(scrapy.Spider):
    name = "fables"
    allowed_domains = ['read.gov']
    start_urls = ['http://www.read.gov/aesop/001.html']

    def parse(self, response):
        TOC_SELECTOR = '//a[@style="toc"]'
        for link in response.xpath(TOC_SELECTOR):
            pageLink = link.xpath('@href').get()
            yield scrapy.Request(
                response.urljoin(pageLink),
                callback=self.parsePage
            )
            # {
            #     'title': link.xpath('text()').get(),
            #     'pageLink': link.xpath('@href').get()
            # }

    def parsePage(self, response):
        TITLE_SELECTOR = '//h1/text()'
        PARAGRAPH_SELECTOR = '//p/text()'
        MORAL_SELECTOR = '//blockquote/text()'

        yield {
            'title': response.xpath(TITLE_SELECTOR).extract_first(),
            'paragraphs': response.xpath(PARAGRAPH_SELECTOR).extract(),
            'moral': response.xpath(MORAL_SELECTOR).extract_first()
        }