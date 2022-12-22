
import scrapy
import pandas as pd
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
from scrapy import FormRequest, Request

class VillageData(scrapy.Spider):
    name = 'ffdata'
    start_urls = ['http://epds.bihar.gov.in/RCList_Village_Wise.aspx?Village_Code_PMO=1020301019216791&&Village_Name_PMO=Bassganw&&Panchayat_Code_PMO=001162&&Panchayat_Name_PMO=BANSGAWNMANJHARIYA&&District_Code_PMO=203&&District_Name_PMO=PashchimChamparan&&Tahsil_Code_PMO=01019&&Tahsil_Name_PMO=Bagaha']

    def parse(self, response):
        pages = response.css('table')[2].css('tr').css('td').css('a::attr(href)').extract()
        tex = response.css('table')[2].css('tr').css('td').css('font ::text').extract()[10]
      
        rows= response.css('table.cellstyle tr')
        for row in rows[1:51]:
            # data = row.css('td').extract()
            yield{
                "SNO": row.css('td')[0].css('span::text').extract()[0],
                "Ration_Card" : "'"+row.css('td')[1].css('a').css('font::text').extract()[0]+"'",
                "Card_Type" : row.css('td')[2].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "Ratio_Card_Holder_Name" : row.css('td')[3].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "Father_Name" : row.css('td')[4].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "Number_of_Family_Members" : row.css('td')[5].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "FPS Dealer" :  row.css('td')[6].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", "") +row.css('td')[6].css('font::text').extract()[1].replace("\r\n", "").replace(" ",""),
                "State" : response.css('table tr').css('td')[1].css('b::text').extract()[0],
                "District": response.css('table tr').css('td')[2].css('b').css('span ::text').extract()[0],
                "Block" : response.css('table tr').css('td')[3].css('b').css('span ::text').extract()[0],
                "Panchayat" :  response.css('table tr').css('td')[4].css('b').css('span ::text').extract()[0],
                "Village":response.css('table tr').css('td')[5].css('b').css('span ::text').extract()[0],
            }
        # for row in range(1,24):    
        for page in pages:
            row= page.split('$')[1].replace("')","")
            # print(row)
            data = {
            '__EVENTTARGET': 'gridmain',
            '__EVENTARGUMENT': 'Page$'+row      
            }
            # print(data)
            yield FormRequest.from_response(response,formdata=data, callback=self.step2)   
        
 
    def step2(self, response):
        # extract data from 
        # pages = response.css('table')[2].css('tr').css('td').css('a::attr(href)').extract()
        # for page in pages[1:]:
        #     row= page.split('$')[1].replace("')","")
        # print(pages)
        rows= response.css('table.cellstyle tr')
        for row in rows[1:51]:
            yield{
                "SNO": row.css('td')[0].css('span::text').extract()[0],
                "Ration_Card" : "'"+row.css('td')[1].css('a').css('font::text').extract()[0]+"'",
                "Card_Type" : row.css('td')[2].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "Ratio_Card_Holder_Name" : row.css('td')[3].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "Father_Name" : row.css('td')[4].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "Number_of_Family_Members" : row.css('td')[5].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", ""),
                "FPS Dealer" :  row.css('td')[6].css('font::text').extract()[0].split('\r\n ')[1].replace(" ", "") +row.css('td')[6].css('font::text').extract()[1].replace("\r\n", "").replace(" ",""),
                "State" : response.css('table tr').css('td')[1].css('b::text').extract()[0],
                "District": response.css('table tr').css('td')[2].css('b').css('span ::text').extract()[0],
                "Block" : response.css('table tr').css('td')[3].css('b').css('span ::text').extract()[0],
                "Panchayat" :  response.css('table tr').css('td')[4].css('b').css('span ::text').extract()[0],
                "Village":response.css('table tr').css('td')[5].css('b').css('span ::text').extract()[0],
            }
            
        


#main drive
# if __name__ == '__main__':
#     # run scraper
#     process = CrawlerProcess()
#     process.crawl(VillageData)
#     process.start()
