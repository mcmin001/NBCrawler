from collections import deque

ershoufang_pages_queue = deque()
ershoufang_detail_url_queue = deque()


def enqueue_ershoufang_page_url(url):
    ershoufang_pages_queue.append(url)


def enqueue_ershoufang_detail_url(url):
    ershoufang_detail_url_queue.append(url)
