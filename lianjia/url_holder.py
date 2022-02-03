from collections import deque


ershoufang_page_queue = deque()


def enqueue_ershoufang_page_url(url):
    ershoufang_page_queue.append(url)
