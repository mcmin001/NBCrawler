from bs4 import BeautifulSoup
from lianjia import url_holder

# 获取每一页中的二手房主页url
def parse_sellListContent(html):
    soup = BeautifulSoup(html, "lxml")
    sellListContent = soup.find("ul", class_="sellListContent")
    if sellListContent is not None:
        # house_li_arr = sellListContent.findAll("li", {"class": {"clear", "LOGCLICKDATA"}})
        # clear LOGCLICKDATA
        house_li_arr = sellListContent.find_all("li", class_="LOGCLICKDATA")
        for li in house_li_arr:
            print(li.a.attrs['href'])
            url_holder.enqueue_ershoufang_detail_url(li.a.attrs['href'])

# 获取链接二手房所有列表页的URL
def generate_page_url(total_page_num):
    page_url = "https://wh.lianjia.com/ershoufang/"
    page_url_list = []
    for i in range(1, total_page_num):
        page_url_list.append(page_url + "pg" + str(i))
        url_holder.ershoufang_page_enqueue(page_url + "pg" + str(i))

