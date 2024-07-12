# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import Join


class NextspaceflightItem(Item):
    organization = Field(output_processor=Join())
    location = Field(output_processor=Join())
    datetime = Field(output_processor=Join())
    details = Field(output_processor=Join())
    price = Field(output_processor=Join())
    status = Field(output_processor=Join())
    mission_status = Field(output_processor=Join())
