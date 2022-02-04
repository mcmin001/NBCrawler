from lianjia_crawler_context import LianJiaCrawlerContext
from crawlerhttp import httputil
import lianjia_parser


def crawler_run():
    count = 0
    # 产生所有列表页的url
    lianjiaCrawlerContext = LianJiaCrawlerContext()
    lianjiaCrawlerContext.generatePageUrl(100)

    for page_url in lianjiaCrawlerContext.getUrlHolder().getErshoufangPagesQueue():
        page_content = httputil.getwebpage(page_url)
        lianjiaCrawlerContext.getUrlHolder().enqueue_ershoufang_detail_urls(
            lianjia_parser.parse_sellListContent(page_content))

    for url in lianjiaCrawlerContext.getUrlHolder().getErshoufangDetailUrlsQueue():
        print(url)
        count = count + 1

    print("一共有" + str(count) + "二手房")



if __name__ == '__main__':
    crawler_run()
