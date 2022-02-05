import unittest

from crawlerhttp import httputil
from lianjia import lianjia_parser


class CrawlerTest(unittest.TestCase):
    #def testLianjia(self):
    #    page_content = httputil.getwebpage("https://wh.lianjia.com/ershoufang/")
    #    print(page_content)
    #    fileutil.write_to_file(page_content, "D:\\test\\page.html")

    def testPageParse(self):
        page_content = httputil.getwebpage("https://wh.lianjia.com/ershoufang/")
        lianjia_parser.parse_sellListContent(page_content)

    def test_generate_page_url(self):
        for url in lianjia_parser.generate_page_url(100):
            print("page url is " + url)

    def test_house_detail(self):
        page_content = httputil.getwebpage("https://wh.lianjia.com/ershoufang/104107909556.html")
        lianjia_parser.parse_house_info(page_content)


if __name__ == '__main__':
    # 运行所有的测试用例
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CrawlerTest("test_generate_page_url"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
