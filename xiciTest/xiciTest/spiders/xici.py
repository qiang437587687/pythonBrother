# -*- coding: utf-8 -*-
import scrapy
from xiciTest.items import XicitestItem
import logging

logging.basicConfig(level=logging.INFO)

class XiciSpider(scrapy.Spider):

    name = "xici"

    allowed_domains = ["xicidaili.com/"]

    start_urls = (
        'http://www.xicidaili.com',
    )

    def start_requests(self):
        reqs = []
        for i in range(1, 5):
            req = scrapy.Request('http://www.xicidaili.com/nn/%s' % i)
            reqs.append(req)
        return reqs

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]')
        trs = ip_list[0].xpath('tr')

        items = []
        # //*[@id="ip_list"]/tbody/tr[1]
        # ip_li = response.xpath('//*[@id="ip_list"]/tbody')  # 我也不知道为什么这个一直是不行的

        for ip in trs[1:]:

            pre_item = XicitestItem()

            pre_item['IP'] = ip.xpath('td[3]/text()')[0].extract()

            pre_item['PORT'] = ip.xpath('td[4]/text()')[0].extract()

            # print(ip.xpath('td[5]/text()')[0].extract())
            pre_item['POSITION'] = ip.xpath('string(td[5])')[0].extract().strip() # 这个地方的用法 有一个string xpath里面可能也是用这个来转换字符串的但是现在这个网页修改了
            # pre_item['POSITION'] = ip.xpath('td[5]/a[0]')[0].extract()

            pre_item['TYPE'] = ip.xpath('td[7]/text()')[0].extract()

            pre_item['SPEED'] = ip.xpath(
                'td[8]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]

            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()

            items.append(pre_item)

        return items

    #昨天 后来不好用了可能是 因为 数据库的事  妈蛋  Crawled (200) <GET http://www.xicidaili.com/nn/1> (referer: None) 到这里
    #Crawled (200) <GET http://www.xicidaili.com/nn/1> (referer: None) 到这里下面就是去pipline里面找数据库的那段了~


    # def parse(self, response):  # //*[@id="ip_list"]  #  网站上下载的原版代码
    #     ip_list = response.xpath('//*[@id="ip_list"]')
    #
    #     trs = ip_list[0].xpath('tr')
    #
    #     items=[]
    #
    #     # ip_tr = response.xpath('//*[@id="ip_list"]/tbody/tr')
    #
    #     for ip in trs[1:]:
    #         pre_item = XicitestItem()
    #
    #         pre_item['IP'] = ip.xpath('td[3]/text()')[0].extract()
    #
    #         pre_item['PORT'] = ip.xpath('td[4]/text()')[0].extract()
    #
    #         pre_item['POSITION'] = ip.xpath('string(td[5])')[0].extract().strip()
    #
    #         pre_item['TYPE'] = ip.xpath('td[7]/text()')[0].extract()
    #
    #         pre_item['SPEED'] = ip.xpath(
    #             'td[8]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
    #
    #         pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()
    #
    #         items.append(pre_item)
    #
    #     return items


