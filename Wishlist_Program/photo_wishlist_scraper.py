import requests
from bs4 import BeautifulSoup
import csv
# import json
# from requests_html import HTMLSession


def main():
    File = open("out.csv", "a")
    # URL = "https://www.keh.com/shop/canon-ef-2751b002-70-mm-200-mm-f-2-8-telephoto-zoom-lens.html"
    # URL = "https://www.bhphotovideo.com/c/product/1547009-REG/canon_eos_r5_mirrorless_digital.html"
    # URL = 'https://www.amazon.com/Canon-Full-Frame-Mirrorless-Megapixel-Processor/dp/B08C68F2DX/ref=sr_1_3?crid=28LFOCBV5G9WA&keywords=canon%2Beos%2Br5&qid=1648054635&sprefix=canon%2Beos%2Br%2Caps%2C353&sr=8-3&th=1'
    # URL = "https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-100mm-f-2-8-macro/"
    # URL = "https://www.cpricewatch.com/product/06708/Canon-RF-24-105mm-F4-L-IS-USM-price.html"
    URL = "https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-70-200mm-f-4-l-usm/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # get_info_canon(soup)
    # session = HTMLSession()
    # response = session.get(URL)
    # amazon_info = get_info_amazon(soup)
    mpb_dict =get_info_mpb(soup)
    # bh_info = get_info_bh(response)
    # keh_info = get_info_keh(soup)
    print (mpb_dict)

def get_info_mpb(soup):
        like_new_price=0
        excellent_price=0
        good_price=0
        well_used_price=0
        like_new=False
        excellent=False
        good=False
        well_used=False
        item_name = soup.find("h1", class_="text-center www-model-name h2").text.strip()
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
        if like_new == False:
            like_new_price = "NA"
        if excellent == False:
            excellent_price = "NA"
        if good == False:
            good_price = "NA"
        if well_used == False:
            well_used_price = "NA"
        mpb_dict = {'Service':'MPB', 'Item_Name': item_name,'Like_New':like_new_price,'Excellent':excellent_price,'Good':good_price,'Well_Used':well_used_price}
        return mpb_dict


def write_to_csv (dicts):
    with open('Wishlist_Program\wishlist.csv', 'w', newline='') as wishlist:
        fieldnames = ['Service','Item_Name','Like_New', 'Excellent', 'Good', 'Well_Used']
        wishlist_writer = csv.DictWriter(wishlist, fieldnames=fieldnames)
        wishlist_writer.writeheader()
        wishlist_writer.writerows(dicts)


# def get_info_bh(response):
#     # soup = BeautifulSoup(response)
#     # price = soup.find("div", class_="price_dx5435RJLV").text.strip()
#     # soup = json.loads("details_IuQVq7UR7J")
#     # for d in soup.select("div[data-selenium=pricingPrice]"):
#         # data = json.loads(d["data-pricingPrice"])
#         # print(data)
#     # driver = webdriver.PhantomJS()
#     # driver.get('https://www.bhphotovideo.com/c/product/1547009-REG/canon_eos_r5_mirrorless_digital.html')
#     # p_element = driver.find_element_by_id(class_='text_v_wGSQBcdt comfy_v_wGSQBcdt sizeTitle1_v_wGSQBcdt weightNormal_v_wGSQBcdt primary_aEALyqkgyT')
#     # print(p_element.text)
#     print(response)

# def get_info_canon(soup):
#     prices = soup.find_all("span", class_="price_link_big")
#     names = soup.find(id_="m.00040.00038.0.0")
#     print(prices)
#     print(names)


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