import requests
from bs4 import BeautifulSoup
import csv
from re import search
# import json
# from requests_html import HTMLSession


def main():
    File = open("out.csv", "a")
    # URL = "https://www.bhphotovideo.com/c/product/1547009-REG/canon_eos_r5_mirrorless_digital.html"
    # URL = 'https://www.amazon.com/Canon-Full-Frame-Mirrorless-Megapixel-Processor/dp/B08C68F2DX/ref=sr_1_3?crid=28LFOCBV5G9WA&keywords=canon%2Beos%2Br5&qid=1648054635&sprefix=canon%2Beos%2Br%2Caps%2C353&sr=8-3&th=1'
    # URL = "https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-100mm-f-2-8-macro/"
    # URL = "https://www.cpricewatch.com/product/06708/Canon-RF-24-105mm-F4-L-IS-USM-price.html"
    URL = "https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-70-200mm-f-2-8-l-is-ii-usm/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    mpb_dict =get_info_mpb(soup)
    URL = "https://www.keh.com/shop/canon-ef-2751b002-70-mm-200-mm-f-2-8-telephoto-zoom-lens.html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    keh_dict = get_info_keh(soup)
    dicts= []
    dicts.append(mpb_dict)
    dicts.append(keh_dict)
    # print (dicts)
    write_to_csv(dicts)

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
    like_new_price=0
    excellent_price=0
    good_price=0
    well_used_price=0
    like_new=False
    excellent=False
    good=False
    well_used=False
    ln = "LN"
    lk_nw_mn= "LN-"
    ex_plus = "EX+"
    ex="EX"
    bgn= "BGN"
    prices=[]
    items = soup.find_all("tr", class_="no-border trigger-a2c-button active")
    item_name = soup.head.title.text.strip().replace(" at KEH Camera","")
    conditions = soup.find_all("td", class_="item-condition text-align center")
    for item in items:
        price = float(item.find("span", class_="price").text.strip().replace("$", "").replace(",",""))
        prices.append(price)
    items = soup.find_all("tr",class_="no-border trigger-a2c-button")
    for item in items:
        price = float(item.find("span", class_="price").text.strip().replace("$", "").replace(",",""))
        prices.append(price)
    for count, value in enumerate(conditions):
        condition = str(value.find("meta"))
        if search(ln, condition):
            like_new = True
            if prices[count] < like_new_price or like_new_price==0:
                like_new_price = float(prices[count])
            # print ("Found!")
        elif search(lk_nw_mn, condition):
            like_new = True
            if prices[count] < like_new_price or like_new_price==0:
                like_new_price = float(prices[count])
            # print ("Found!")
        elif search(ex_plus, condition):
            excellent = True
            if prices[count] < excellent_price or excellent_price==0:
                excellent_price = float(prices[count])
            # print ("Found!")
        elif search(ex, condition):
            good = True
            if prices[count] < good_price or good_price==0:
                good_price = float(prices[count])    
        elif search(bgn, condition):
            well_used = True
            if prices[count] < well_used_price or well_used_price==0:
                well_used_price = float(prices[count])
    if like_new == False:
        like_new_price = "NA"
    elif excellent == False:
        excellent_price = "NA"
    elif good == False:
        good_price = "NA"
    elif well_used == False:
        well_used_price = "NA"
    keh_dict = {'Service':'KEH', 'Item_Name': item_name,'Like_New':like_new_price,'Excellent':excellent_price,'Good':good_price,'Well_Used':well_used_price}
    # print(keh_dict)
    return keh_dict


main()