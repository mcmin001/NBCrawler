import collections


class UrlHolder:
    def __init__(self):
        self.ershoufang_pages_queue = collections.deque()
        self.ershoufang_detail_url_queue = collections.deque()

    def enqueue_ershoufang_page_url(self, url):
        self.ershoufang_pages_queue.append(url)

    def enqueue_ershoufang_detail_url(self, url):
        self.ershoufang_detail_url_queue.append(url)

    def enqueue_ershoufang_detail_urls(self, urls):
        self.ershoufang_detail_url_queue.extend(urls)

    def getErshoufangPagesQueue(self):
        return self.ershoufang_pages_queue

    def getErshoufangDetailUrlsQueue(self):
        return self.ershoufang_detail_url_queue
