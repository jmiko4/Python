import requests
from bs4 import BeautifulSoup
import json


def main():
    # URL = "https://www.keh.com/shop/canon-ef-2751b002-70-mm-200-mm-f-2-8-telephoto-zoom-lens.html"
    # URL = "https://www.bhphotovideo.com/c/product/1547009-REG/canon_eos_r5_mirrorless_digital.html"
    URL = "https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-100mm-f-2-8-macro/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    mpb_info = get_info_mpb(soup)
    # bh_info = get_info_bh(soup)
    # keh_info = get_info_keh(soup)
    print (mpb_info)

def get_info_mpb(soup):
    info_dict={}
    like_new_price=0
    excellent_price=0
    good_price=0
    well_used_price=0
    like_new=False
    excellent=False
    good=False
    well_used=False
    item_name = soup.find("h1", class_="text-center www-model-name h2")
    items = soup.find_all("article", class_="theme-product-stack-tile jq-theme-stack-tile www-product-list-item")

    for item in items:
        item_price = item.find("strong", class_="www-product-price").text.strip().replace("$", "").replace(",","")
        item_condition = item.find("td", class_="theme-meta-rating www-product-condition").text.strip()

        if item_condition =="Like New":
            like_new = True
            if float(item_price) < like_new_price or like_new_price==0:
                like_new_price = float(item_price)

        if item_condition =="Excellent":
            excellent = True
            if float(item_price) < excellent_price or excellent_price==0:
                excellent_price = float(item_price)
        
        if item_condition =="Good":
            good = True
            if float(item_price) < good_price or good_price==0:
                good_price = float(item_price)
        
        if item_condition =="Well Used":
            well_used = True
            if float(item_price) < well_used_price or well_used_price==0:
                well_used_price = float(item_price)
    if like_new:
        info_dict["Like New"] = like_new_price
    if excellent:
        info_dict["Excellent"] = excellent_price
    if good:
        info_dict["Good"] = good_price
    if well_used:
        info_dict["Well Used"] = well_used_price

    return info_dict

def get_info_bh(soup):
    # price = soup.find("div", class_="price_dx5435RJLV").text.strip()
    # soup = json.loads("details_IuQVq7UR7J")
    for d in soup.select("div[data-selenium=pricingPrice]"):
        data = json.loads(d["data-pricingPrice"])
        print(data)

def get_info_keh(soup):
    items = soup.find_all("tr", class_="no-border trigger-a2c-button active")
    for item in items:
        price = item.find("span", class_="price").text.strip()
        print(price)
    items = soup.find_all("tr",class_="no-border trigger-a2c-button")
    for item in items:
        price = item.find("span", class_="price").text.strip()
        print(price)


main()