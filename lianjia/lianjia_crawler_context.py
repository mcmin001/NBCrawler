from lianjia.url_holder import UrlHolder


class LianJiaCrawlerContext:
    def __init__(self):
        self.urlHoler = UrlHolder()

    def getUrlHolder(self):
        return self.urlHoler

    # 获取链接二手房所有列表页的URL
    def generatePageUrl(self, total_page_num):
        page_url = "https://wh.lianjia.com/ershoufang/"
        page_url_list = []
        for i in range(1, total_page_num + 1):
            page_url_list.append(page_url + "pg" + str(i))
            self.urlHoler.enqueue_ershoufang_page_url(page_url + "pg" + str(i))
