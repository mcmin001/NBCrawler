import requests
from logger import crawler_logger
from crawlerhttp import http_header_generator
from core import crawler_enum

def getwebpage(page_url):
    response = requests.get(page_url, http_header_generator.get_http_header(crawler_enum.CrawlerUserAgent.Microsoft_Edge_69.value))
    response.encoding = 'utf-8'
    if response is not None:
        response_coce = response.status_code
        if response_coce == 200:
            page_content = response.text
            crawler_logger.get_logger().info("request %s success. response content=%s", page_url, page_content)
        else:
            crawler_logger.error("request %s error. response code=%s", page_url, response_coce)
