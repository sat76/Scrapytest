from scrapy.crawler import CrawlerProcess
import unittest
from pricelist.spiders.productspider import PricelistSpider


class PricelistSpiderTest(unittest.TestCase):

    def setUp(self):
        pass

    def _test_item_results(self, results, expected_length):
        count = 0
        permalinks = set()
        for item in results:
            self.assertIsNotNone(item['content'])
            self.assertIsNotNone(item['title'])
        self.assertEqual(count, expected_length)

    def test_parse(self):
        results = self.spider.parse(fake_response_from_file('osdir/sample.html'))
        self._test_item_results(results, 10)

#process.crawl(MySpider)
#process.start() # the process halts for spider to finish
 