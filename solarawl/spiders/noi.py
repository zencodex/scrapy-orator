# -*- coding: utf-8 -*-
import scrapy
from w3lib.html import remove_tags
from models.noi2018_award import Noi2018Award

class NoiSpider(scrapy.Spider):
    name = 'noi'
    allowed_domains = ['www.noi.cn']
    start_urls = [
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/2.htm',
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/t2.htm',
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/t3.htm',
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/1.htm',
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/p2.htm',
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/p3.htm'
    ]

    map_urls = {
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/2.htm':  {'award_type': '复赛提高组一等奖', 'type': 1},
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/t2.htm': {'award_type': '复赛提高组二等奖', 'type': 1},
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/t3.htm': {'award_type': '复赛提高组三等奖', 'type': 1},
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/1.htm':  {'award_type': '复赛普及组一等奖', 'type': 2},
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/p2.htm': {'award_type': '复赛普及组二等奖', 'type': 2},
        'https://www.ccf.org.cn/ccf/preview/zgjsjxh/noi/noi2018/p3.htm': {'award_type': '复赛普及组三等奖', 'type': 2}
    }

    def parse(self, response):

        if (self.map_urls[response.request.url]['type'] == 1):
            nodes = response.xpath("//tr[contains(@style, 'HEIGHT: 18pt; mso-height-source: userset') and not(contains(@class, 'xl6627142'))]")
        else:
            nodes = response.xpath("//*[contains(@style,'HEIGHT: 18pt; mso-height-source: userset')]")

        for node in nodes:
            cols = node.css('td').extract()
            card_no = remove_tags(cols[0])
            table = Noi2018Award.first_or_new(card_no=card_no)
            table.award_type = self.map_urls[response.request.url]['award_type']
            table.exam_no = remove_tags(cols[1])
            table.province = remove_tags(cols[2])
            table.student_name = remove_tags(cols[3])
            table.sex = remove_tags(cols[4])
            table.score = remove_tags(cols[5])
            table.school_name = remove_tags(cols[6])
            table.set_attribute('class', remove_tags(cols[7]))

            if (self.map_urls[response.request.url]['type'] == 1):
                table.mark = remove_tags(cols[8])

            table.save()

        pass
