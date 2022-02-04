from bs4 import BeautifulSoup


# 获取每一页中的二手房主页url
def parse_sellListContent(html):
    ershoufang_detail_url_arr = []
    soup = BeautifulSoup(html, "lxml")
    sellListContent = soup.find("ul", class_="sellListContent")
    if sellListContent is not None:
        # house_li_arr = sellListContent.findAll("li", {"class": {"clear", "LOGCLICKDATA"}})
        # clear LOGCLICKDATA
        house_li_arr = sellListContent.find_all("li", class_="LOGCLICKDATA")
        for li in house_li_arr:
            print(li.a.attrs['href'])
            ershoufang_detail_url_arr.append(li.a.attrs['href'])
    return ershoufang_detail_url_arr
