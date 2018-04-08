# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import GithubItem
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    #allowed_domains = ['github.com']

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for repository in response.css('li.public'):
            item = GithubItem({
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first() 
})
            repository_url = response.urljoin(repository.xpath('.//a/@href').extract_first())
            request = scrapy.Request(repository_url, callback=self.parse_detail)
            request.meta['item'] = item

            yield request

    def parse_detail(self, response):
        item = response.meta['item']
        '''
        item['commits'] = response.xpath('//a[@href="/shiyanlou/louplus-python/commits/master"]/span/text()').re_first('[^\d]*(\d*)[^\d*]')
        item['branches'] = response.xpath('//a[@href="/shiyanlou/louplus-python/branches"]/span/text()').re_first('[^\d]*(\d*)[\d*]')
        item['releases'] = response.xpath('//a[@href="/shiyanlou/louplus-python/releases"]/span/text()').re_first('[^\d]*(\d*)[^\d*]')
        '''

        item['commits'] = re.findall('[^\d]*(\d*)[^\d]*',response.xpath('//span[@class="num text-emphasized"]').extract()[0])[0]
        item['branches'] = re.findall('[^\d]*(\d*)[^\d]*',response.xpath('//span[@class="num text-emphasized"]').extract()[1])[0]
        item['releases'] = re.findall('[^\d]*(\d*)[^\d]*',response.xpath('//span[@class="num text-emphasized"]').extract()[2])[0]
        yield item
