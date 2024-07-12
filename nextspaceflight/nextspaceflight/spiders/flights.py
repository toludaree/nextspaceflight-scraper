
from nextspaceflight.items import NextspaceflightItem
from itemloaders import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FlightsSpider(CrawlSpider):
    name = "flights"
    allowed_domains = ["nextspaceflight.com"]
    start_urls = ["https://nextspaceflight.com/launches/past/?page=1&search="]
    
    rules = (
        # Space FLight Details
        Rule(
            LinkExtractor(
                restrict_xpaths="//div[contains(@class, 'mdl-cell')]" \
                                "//a[contains(@href, '/launches/details/')]"
            ),
            callback="parse",
            follow=True
        ),
        # Next Page
        Rule(
            LinkExtractor(
                restrict_xpaths="//span[@class='step-links']//a[span='next']"
            ),
            callback="parse",
            follow=True
        ),
    )

    def parse(self, response):
        item = ItemLoader(item=NextspaceflightItem(),
                          response=response,
                          selector=response)
        item.add_xpath("organization",
                       "//h3[contains(text(), 'Rocket')]" \
                       "/following::section[1]" \
                       "//div[contains(@class, 'mdl-cell--12-col-tablet')][1]" \
                       "/text()")
        item.add_xpath("location",
                       "//h3[contains(text(), 'Location')]" \
                       "/following::section[1]//h4/text()")
        item.add_xpath("datetime",
                       "//h3[contains(text(), 'Status')]" \
                       "/following::section[1]" \
                       "//div[@class='mdl-cell']/span/text()")
        
        item.add_xpath("details",
                       "//h3[contains(text(), 'Mission Details')]" \
                       "/following::section[1]//h4/text()")
        item.add_xpath("details",
                       "//h3[contains(text(), 'Mission Details')]" \
                       "/following::section[1]//p/text()")
        item.add_value("details", "break")    # divides the details field in 2
        item.add_xpath("details",
                       "//h3[contains(text(), 'Mission Details')]" \
                       "/following::section[1]" \
                       "//div[@class='mdl-cell']/text()")
        
        item.add_xpath("price",
                       "//h3[contains(text(), 'Rocket')]" \
                       "/following::section[1]" \
                       "//div[contains(@class, 'mdl-cell--12-col-tablet')][3]" \
                       "/text()")
        item.add_xpath("status",
                       "//h3[contains(text(), 'Rocket')]" \
                       "/following::section[1]" \
                       "//div[contains(@class, 'mdl-cell--12-col-tablet')][2]" \
                       "/text()")
        item.add_xpath("mission_status",
                       "//h3[contains(text(), 'Status')]" \
                       "/following::section[1]" \
                       "/h6[contains(@class, 'status')]/span/text()")

        yield item.load_item()
