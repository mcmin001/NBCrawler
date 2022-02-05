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


def parse_house_info(html):
    soup = BeautifulSoup(html, "lxml")
    totalPrice = ""
    # 获取总价
    priceContainerDiv = soup.find("div", class_="price-container")
    if priceContainerDiv is not None:
        priceDiv = priceContainerDiv.find("div", class_="price")
        if priceDiv is not None:
            totalSpan = priceDiv.find("span", class_="total")
            if totalSpan is not None:
                totalPrice = totalSpan.text
        unitPriceValueSpan = priceContainerDiv.find("span", class_="unitPriceValue")
        if unitPriceValueSpan is not None:
            print(unitPriceValueSpan.text)
    # 获取单价 元/平米




