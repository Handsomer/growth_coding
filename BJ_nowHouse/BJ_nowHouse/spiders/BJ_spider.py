# -*- coding: utf-8 -*-
import scrapy
import logging

from BJ_nowHouse.items import BjNowhouseItem

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 文本设置
fh = logging.FileHandler("tmp.log")
fh.setLevel(logging.DEBUG)
# 设置日期
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


class BeiJingSpider(scrapy.Spider):
    name = 'Beijing_data'
    # start_urls = ('http://www.bjjs.gov.cn')
    start_urls = (
    'http://www.bjjs.gov.cn/eportal/ui?pageId=308452&ddlQX=-1&ddlQW=-1&isTure=ture&rblFWType1=x&currentPage=' + str(i)
    for i in range(1, 2))

    #	def start_requests(self):
    #		reqs = []
    # 枚举的所有页面的url
    #		for i in range(1,207):
    #			reqs.append('http://www.bjjs.gov.cn/eportal/ui?pageId=308452&ddlQX=-1&ddlQW=-1&isTure=ture&rblFWType1=x&currentPage=' + str(i))
    #		return reqs

    def parse(self, response):
        tmp = response.xpath('//*[@id="FDCJYFORM"]/table[2]/tr[2]/td/table/tr')
        for i in tmp:
            # 获得每个小区详情的URL
            tmp1 = i.xpath('td[2]/a/@href').extract_first()
            if tmp1 and len(tmp1):
                print '---', tmp1
                detail_url = response.urljoin(tmp1)
                # 打开小区的详情页，解析出小区的详情
                yield scrapy.Request(detail_url, callback=self.parse_XiaoQu_detail)

    def parse_XiaoQu_detail(self, response):
        # 获取小区详情
        tmp = response.xpath("//*[@id='XMmanage']/table[2]/tr")
        project_name = tmp[1].xpath('td[2]/span/text()').extract_first()
        local_place = tmp[2].xpath('td[2]/span/text()').extract_first()
        publish_date = tmp[5].xpath('td[2]/span/text()').extract_first()
        logger.debug("xiaoqu project_name: %s", project_name)
        logger.debug("xiaoqu local_place: %s", local_place)
        logger.debug("xiaoqu publish_date: %s", publish_date)
        # 获得楼盘表里，查看信息的URl
        louhao_list = response.xpath('//*[@id="table_floorTray"]/tr')
        for lou_detail in louhao_list[2:]:
            lou_detail_list = lou_detail.xpath('td')
            lou_detail_msg_url = response.urljoin(lou_detail_list[-1].xpath('a/@href').extract_first())
            if lou_detail_msg_url:
                logger.debug("xiaoqu response.url: %s", response.url)
                logger.debug("loufnag lou_detail_msg_url: %s", lou_detail_msg_url)
                yield scrapy.Request(lou_detail_msg_url,
                                     meta={"project_name": project_name, "local_place": local_place,
                                           "publish_date": publish_date},
                                     callback=self.make_house_url)

    def make_house_url(self, response):
        tmp = response.xpath('//*[@id="table_Buileing"]/tbody/tr')
        for elem in tmp[1:]:
            for sub_elem in elem.xpath('td')[-1].xpath('div'):
                # 获得房屋的url
                house_url = sub_elem.xpath('a/@href').extract_first()
                if house_url != u'#':
                    target_house_url = response.urljoin(house_url)
                    # 采集房屋信息
                    yield scrapy.Request(target_house_url,
                                         meta=response.meta,
                                         callback=self.get_house_detail)

    def get_house_detail(self, response):
        ''' 
		project_name = scrapy.Field()
	    local_place = scrapy.Field()
	    publish_date = scrapy.Field()

	    use_for = scrapy.Field()
	    build_area = scrapy.Field()
	    build_in_area = scrapy.Field()
	    sale_for_build = scrapy.Field()
	    sale_for_build_in = scrapy.Field()
		'''
        HouseItem = BjNowhouseItem()
        tmp = response.xpath('//*[@id="showDiv"]/table/tr')
        try:
            HouseItem['project_name'] = response.meta['project_name']
            HouseItem['local_place'] = response.meta['local_place']
            HouseItem['publish_date'] = response.meta['publish_date']
            HouseItem['use_for'] = tmp[1].xpath('td[2]/text()').extract_first().split()[0]
            HouseItem['build_type'] = tmp[2].xpath('td[2]/text()').extract_first().split()[0]
            HouseItem['build_area'] = tmp[3].xpath('td[2]/text()').extract_first().split()[0]
            HouseItem['build_in_area'] = tmp[4].xpath('td[2]/text()').extract_first().split()[0]
            HouseItem['sale_for_build'] = tmp[5].xpath('td[2]/text()').extract_first().split()[0]
            HouseItem['sale_for_build_in'] = tmp[6].xpath('td[2]/text()').extract_first().split()[0]
        except:
            logger.error('''get contend error\n
				--use_for:%s\n--build_type:%s\n--build_area:%s\n--build_in_area:%s\n--sale_for_build:%s\n--sale_for_build_in:%s\n''',
                         tmp[1].xpath('td[2]/text()').extract_first().split()[0],
                         tmp[2].xpath('td[2]/text()').extract_first().split()[0],
                         tmp[3].xpath('td[2]/text()').extract_first().split()[0],
                         tmp[4].xpath('td[2]/text()').extract_first().split()[0],
                         tmp[5].xpath('td[2]/text()').extract_first().split()[0],
                         tmp[6].xpath('td[2]/text()').extract_first().split()[0])
        finally:
            error_msg = ''
            for key in HouseItem.keys():
                error_msg += HouseItem[key]
            logger.debug('get houseItem msg: %s', error_msg)
            logger.debug('house_url:%s', response.url)
            yield HouseItem



