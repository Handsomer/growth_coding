from scrapy.selector import Selector
from scrapy import Spider
from search_the_world.items import SearchTheWorldItem


class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_page","https://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        item = SearchTheWorldItem()
        title = response.xpath('//h1/text()')[0].extract()
        print("title is : "+ title)
        item['title'] = title
        return item
