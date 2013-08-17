from crunchbase.items import CrunchbaseItem
from urlparse import urlparse

class CrunchbaseDataParser:    
    @staticmethod
    def extract_item(x):
        item = CrunchbaseItem()
        business_name = x.select("//div[@id='col2_internal']/h1[@class='h1_first']/text()[1]").extract()
        if CrunchbaseDataParser.not_empty(business_name):
            item['business_name'] = business_name[0].strip(" \t\n\r")
                
        about = x.select("//div[@id='col2_internal']/p/text()").extract()
        if CrunchbaseDataParser.not_empty(about):
            item['about'] = '<br/>'.join(x.strip(" \t\n\r") for x in about)
                  
        address = x.select("//div[@id='col1']/div[@class='col1_content']/div[@class='col1_office_address']")
        street_address = address.select('text()').extract()
        if CrunchbaseDataParser.not_empty(street_address):
            item['street_address'] = street_address[0].strip()
               
  
        city = address.select(".//a[contains(@href, 'city')]/text()").extract()
        if CrunchbaseDataParser.not_empty(city):
            item['city'] = city[0].strip()
                   
        state = address.select(".//a[contains(@href, 'state')]/text()").extract()
        if CrunchbaseDataParser.not_empty(state):
            item['state'] = state[0].strip()
                
        zip_code = address.select(".//a[contains(@href, 'zip')]/text()").extract()
        if CrunchbaseDataParser.not_empty(zip_code):
            item['zip_code'] = zip_code[0].strip()
                   
        country = address.select(".//a[contains(@href, 'country')]/text()").extract()
        if CrunchbaseDataParser.not_empty(country):
            item['country'] = country[0].strip()
                
        tables = x.select("//div[@id='col1']/div[@class='col1_content']/table")
        for tr in tables.select(".//tr"):
            label = tr.select(".//td[@class='td_left']/text()").extract()
            if CrunchbaseDataParser.not_empty(label):
                l = label[0].strip(" \t\n\r").lower()
                if l == 'website':
                    v = tr.select(".//td[@class='td_right']/a/@href").extract()
                    if CrunchbaseDataParser.not_empty(v):
                        domain = v[0].strip(" \t\n\r")
                        item['website'] = domain
                    
                elif l == 'email':
                    v = tr.select(".//td[@class='td_right']/a/@title").extract()
                    if CrunchbaseDataParser.not_empty(v):
                        item['email'] = v[0].strip(" \t\n\r")
                   
                elif l == 'phone':
                    v = tr.select(".//td[@class='td_right']/text()").extract()
                    if CrunchbaseDataParser.not_empty(v):
                        item['phone'] = v[0].strip(" \t\n\r")
                    
                elif l == 'category':
                    v = tr.select(".//td[@class='td_right']/a/text()").extract()
                    if CrunchbaseDataParser.not_empty(v):
                        item['category'] = v[0].strip(" \t\n\r")
                    
        return item
    @staticmethod
    def not_empty(data):
        if data and len(data) >= 1:
            return True
        return False
