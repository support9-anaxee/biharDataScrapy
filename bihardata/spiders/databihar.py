import scrapy
import pandas as pd
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess

class VillageData(scrapy.Spider):
    name = 'ffdata'

    def start_requests(self):
        urls = [
            'http://epds.bihar.gov.in/RCList_Village_Wise.aspx?Village_Code_PMO=1020301019216791&&Village_Name_PMO=Bassganw&&Panchayat_Code_PMO=001162&&Panchayat_Name_PMO=BANSGAWNMANJHARIYA&&District_Code_PMO=203&&District_Name_PMO=PashchimChamparan&&Tahsil_Code_PMO=01019&&Tahsil_Name_PMO=Bagaha'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # extract data from 
        rows= response.css('table.cellstyle tr')
        for row in rows[1:]:
            # data = row.css('td').extract()
            name = {
                "SNO": row.css('td').css('span::text').extract()[0],
                "Ration Card" : row.css('td').css('a').css('font::text').extract()[0],
                "Card Type" : row.css('td')
            }
            print(name)
            
            # name = {
            #         "SNO" : row.css('span::text').css('span::text'),
            #         "RationCard": row.css('a').css('font::text').extract_first(),
            #         "Card Type" : row.css('a')[0],
            #     }
            # print("@@@", name)
            # for data in row.css('td'):
                
            

        # open_in_browser(response)

#main drive
# if __name__ == '__main__':
#     # run scraper
#     process = CrawlerProcess()
#     process.crawl(VillageData)
#     process.start()
