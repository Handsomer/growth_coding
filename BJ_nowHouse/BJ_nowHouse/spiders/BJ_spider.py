import scrapy 
from BJ_nowHouse.items import BjNowhouseItem

class BeiJingSpider(scrapy.Spider):
	name = 'Beijing_data'
	start_urls = ('http://www.bjjs.gov.cn/eportal/ui?pageId=308452&ddlQX=-1&ddlQW=-1&isTure=ture&rblFWType1=x&currentPage=' + str(i) for i in range(1,207))

	def parse(self, response):
		tmp = response.xpath('//*[@id="FDCJYFORM"]/table[2]/tr[2]/td/table/tr')
		for i in tmp:
			tmp1 = i.xpath('td[2]/a/@href').extract_first()
			if tmp1 and len(tmp1):
				print '---',tmp1
				detail_url = response.urljoin(tmp1)
				yield scrapy.Request(detail_url, callback=self.parse_detail)

	def parse_detail(self,response):

		tmp = response.xpath("//*[@id='XMmanage']/table[2]/tr")
		item = BjNowhouseItem()
		item['project_name'] = tmp[2].xpath('td[2]/span/text()').extract_first()
		item['local_place'] = tmp[3].xpath('td[2]/span/text()').extract_first()
		item['publish_date'] = tmp[6].xpath('td[2]/span/text()').extract_first()
		yield item
