import requests
from bs4 import BeautifulSoup
import csv
from re import search


def main():
    File = open("out.csv", "a")
    URL_MPB = "https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-70-200mm-f-2-8-l-is-ii-usm/"
    mpb_dict =get_info_mpb(URL_MPB)
    URL_KEH = "https://www.keh.com/shop/canon-ef-2751b002-70-mm-200-mm-f-2-8-telephoto-zoom-lens.html"
    keh_dict = get_info_keh(URL_KEH)
    dicts= []
    dicts.append(mpb_dict)
    dicts.append(keh_dict)
    # print (dicts)
    write_to_csv(dicts)
    csv_reader('Wishlist_Program/wishlist.csv')

def get_info_mpb(URL):
    '''Takes an MPB link and returns a dictionary with product information and pricing'''
    like_new_price=0
    excellent_price=0
    good_price=0
    well_used_price=0
    like_new=False
    excellent=False
    good=False
    well_used=False
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
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
    """Writes several dictionaries to a CSV file from a list of dictionaries"""
    with open('Wishlist_Program\wishlist.csv', 'w', newline='') as wishlist:
        fieldnames = ['Service','Item_Name','Like_New', 'Excellent', 'Good', 'Well_Used']
        wishlist_writer = csv.DictWriter(wishlist, fieldnames=fieldnames)
        wishlist_writer.writeheader()
        wishlist_writer.writerows(dicts)

def csv_reader(file):
    '''Takes a CSV file name and opens and reads it into a list then returns that list'''
    SERVICE = 0
    ITEM_NAME = 1
    LIKE_NEW = 2
    EXCELLENT = 3
    GOOD = 4
    WELL_USED=5
    csv_list =[]
    with open(file) as kyle:  
        reader = csv.reader(kyle)
        for line in reader:
            csv_list.append(line)
    return csv_list

def get_info_keh(URL):
    '''Takes a KEH link and returns a dictionary with product information and pricing'''
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
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
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