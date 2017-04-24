# -*- coding: utf-8 -*-
import scrapy
import logging

from BJ_nowHouse.items import GzNowhouseItem

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 文本设置
fh = logging.FileHandler("tmp.log")
fh.setLevel(logging.DEBUG)
# 设置日期
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

class GuangZhouSpider(scrapy.Spider):
    name = 'Guangzhou_data'
    start_urls = (
        "http://www.gzcc.gov.cn/laho/ProjectSearch.aspx/ProjectSearch.aspx?page=" + str(i)
        for i in range(1,367))
    def parse(self, response):
        tmp = response.xpath('//*[@class="resultTableC"]/tbody/tr')
        base_url = 'http://www.gzcc.gov.cn//laho/project.aspx?'
        for elem in tmp[1:]:
            item = {}
            item['project_name'] = elem.xpath('td')[1].xpath('a/text()').extract_first()
            item['developr'] = elem.xpath('td')[2].xpath('a/text()').extract_first()
            item['local_place'] = elem.xpath('td')[4].xpath('a/text()').extract_first()
            xiaoqu_url = elem.xpath('td')[2].xpath('a/@href').extract_first()
            PID = xiaoqu_url[xiaoqu_url.find('pjID='):xiaoqu_url.find('&name')]
            target_xiaoqu_url = base_url + PID
            logger.debug('project_name:%s',elem.xpath('td')[1].xpath('a/text()').extract_first())
            logger.debug('developr:%s', elem.xpath('td')[2].xpath('a/text()').extract_first())
            logger.debug('local_place:%s', elem.xpath('td')[4].xpath('a/text()').extract_first())
            logger.debug('target_xiaoqu_url:%s', target_xiaoqu_url)
            yield scrapy.Request(target_xiaoqu_url,meta = item,callback=self.parse_detail)

    def parse_detail(self,response):
        '''
        saledHouse_num = scrapy.Field()
        unsaledHouse_num = scrapy.Field()
        area = scrapy.Field()
        saled_area = scrapy.Field()
        unsaled_area = scrapy.Field()
        price = scrapy.Field()
        '''
        item = GzNowhouseItem()
        item['project_name'] = response.meta['project_name']
        item['developr'] = response.meta['developr']
        item['local_place'] = response.meta['developr']
        item['area'] = response.xpath('//*[@class="content"]/table[1]/tr[4]/td[2]/text()').extract_first()
        item['saledHouse_num'] = response.xpath('//*[@class="content"]/table[1]/tr[4]/td[2]/text()').extract_first()
        item['saled_area'] = response.xpath('//*[@class="content"]/table[2]/tr[3]/td[6]/text()').extract_first()
        item['unsaledHouse_num'] = response.xpath('//*[@class="content"]/table[2]/tr[3]/td[8]/text()').extract_first()
        item['unsaled_area'] = response.xpath('//*[@class="content"]/table[2]/tr[3]/td[9]/text()').extract_first()
        item['price'] = response.xpath('//*[@class="content"]/table[2]/tr[3]/td[7]/text()').extract_first()
        logger.debug('area:%s', item['area'])
        logger.debug('saledHouse_num:%s', item['saledHouse_num'])
        logger.debug('saled_area:%s', item['saled_area'])
        logger.debug('unsaledHouse_num:%s', item['unsaledHouse_num'])
        logger.debug('unsaled_area:%s', item['unsaled_area'])
        logger.debug('price:%s', item['price'])
        yield item




