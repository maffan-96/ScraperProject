from scrapy import signals
from scrapy.signalmanager import dispatcher
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from spiders.sreality_apartments import SrealityApartmentsSpider


results = []


def crawler_results(item):
    results.append(item)


def crawl():
    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    settings = {
        'ROBOTSTXT_OBEY': False,
        'LOG_ENABLED': False,
        'LOG_STDOUT': False,
        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
        'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    }
    process = CrawlerProcess(settings)
    process.crawl(SrealityApartmentsSpider)
    process.start()

    return results

if __name__ == '__main__':
    crawl()
