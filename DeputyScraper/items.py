# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Deputy(Item):
    id   = Field()
    name = Field()
    url  = Field()
    seat = Field()
    mail = Field()
    party     = Field()
    election  = Field()
    header    = Field()
    state     = Field()
    onomastic = Field()
    substitute = Field()
    circunscription = Field()
#    page = Field()
#    last_update = Field()
