# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ExampleSpider(CrawlSpider):
    name = 'search'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/']

    print "-"*50
    print "Started crawling for domain(s): "+str(allowed_domains)
    print "-"*50
    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #searchObj = re.findall( r'(aws|api|encryption|access|private|secret)(.?:|_|-|)(key|secret|token|id)(?:\s|)(?:\:|=)', response.body, re.I)
        searchObj = re.findall( r'(aws|api|encryption|private|secret)(.?:|_|-|)(key|secret|token|id)(.?:\s|)*(.?:\:|\=)(?:\s|)(?:\'(.*?)\'|\"(.*?)\")', response.body, re.I)
        # Removed access[_-]token match
        searchClient = re.findall( r'(client|app)(.?:|_|-|)(key|secret|token)(?:\s|)*(.?:\:|=)(?:\s|)(?:\'(.*?)\'|\"(.*?)\")', response.body, re.I)
        searchAWS = re.findall( r'(AWS_SECRET_ACCESS|AWS_SECRET_KEY|secret)(?:\s|)*(.?:\:|=)(?:\s|)(?:\'(.*?)\'|\"(.*?)\")', response.body, re.I)

        if searchObj or searchClient or searchAWS:

          for x in searchObj:
            if len(x)>4:
                print "\r\n[*]Found in URL: "+response.url
                print '[!]'+''.join(x)


          for x in searchClient:
            if len(x)>4:
                print "\r\n[*]Found in URL: "+response.url
                print '[!]'+''.join(x)

          for x in searchAWS:
            if len(x)>2:
                print "\r\n[*]Found in URL: "+response.url
                print '[!]'+''.join(x)
