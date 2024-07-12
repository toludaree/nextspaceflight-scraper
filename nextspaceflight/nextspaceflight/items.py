# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import Join, MapCompose


def details_in(d):
    return d.replace("’", "'")

def details_out(d):
    divider = d.index("break")  # get the index of the divider
    name = d[0]
    mission_details = "\n".join(d[1:divider])
    
    if d[-1] == "break":
        payloads = ""
        total_mass = ""
        orbit_type = ""
    else:
        rest = d[divider+1:]
        if len(rest) == 1:
            payloads = ""
            total_mass = ""
            orbit_type = rest[0].strip()
        elif len(rest) == 2:
            payloads = rest[0].strip().split("Payloads: ")[-1]
            total_mass = ""
            orbit_type = rest[1].strip()
        elif len(rest) == 3:
            payloads = rest[0].strip().split("Payloads: ")[-1]
            total_mass = rest[1].strip().split("Total Mass: ")[-1]
            orbit_type = rest[2].strip()

    return {
        "name": name,
        "mission_details": mission_details,
        "payloads": payloads,
        "total_mass": total_mass,
        "orbit_type": orbit_type
    }

def price_in(d):
    if d.startswith("Price"):
        return d.split("Price: ")[-1]
    return ""
    
def status_in(d):
    return d.split("Status: ")[-1]
    

class NextspaceflightItem(Item):
    organization = Field(output_processor=Join())
    location = Field(output_processor=Join())
    datetime = Field(output_processor=Join())
    details = Field(input_processor=MapCompose(details_in),
                    output_processor=details_out)
    price = Field(input_processor=MapCompose(price_in),
                  output_processor=Join())
    status = Field(input_processor=MapCompose(status_in),
                   output_processor=Join())
    mission_status = Field(output_processor=Join())
