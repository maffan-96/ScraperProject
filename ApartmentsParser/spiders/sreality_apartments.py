import scrapy
from unicodedata import normalize
from items import ApartmentsParserItem

class SrealityApartmentsSpider(scrapy.Spider):
    name = 'sreality_apartments'
    allowed_domains = ['sreality.cz']
    start_urls = ['https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=500']

    def parse(self, response):
        data = response.json()

        for estate in data.get("_embedded", {}).get("estates", []):
            apartment = ApartmentsParserItem()
            apartment["name"] = normalize('NFKD', estate.get('name', ''))
            images = estate.get("_links", {}).get("images", [])
            apartment["img_url"] = images[0]["href"] if images else ''

            yield apartment

