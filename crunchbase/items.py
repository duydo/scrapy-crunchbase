# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class CrunchbaseItem(Item):
    business_name = Field()
    email = Field()
    phone = Field()
    website = Field()
    about = Field()
    street_address = Field()
    city = Field()
    state = Field()
    zip_code = Field()
    country = Field()
    category = Field()
    
    
