import requests
from bs4 import BeautifulSoup
import csv
from re import search
import PySimpleGUI as sg

def main():
    '''Sets up and opens GUI'''
    lists=[]
    sg.theme('Dark Grey 13')
    filename = "Wishlist_Program/wishlist.csv"
    data = []
    header_list = []
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        header_list = next(reader)
        data = list(reader) 
    sg.set_options(element_padding=(0, 0))
    layout = [  [sg.Text('Welcome to the Wishlist Program, Add a KEH or MPB url')],
                [sg.Text('URL'), sg.InputText(do_not_clear=False)],
                [sg.Button('Add Item URL'), sg.Button('Refresh Prices')],
                [sg.Table(values=data,
                            key = "table",
                            headings=header_list,
                            auto_size_columns=True,
                            justification='right',
                            max_col_width=30,
                            alternating_row_color='black',
                            num_rows=min(len(data), 20)
                            )]
                ]
    # Create the Window
    window = sg.Window('Wishlist', layout,finalize=True)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Add Item URL':
            write_url_to_csv(values[0])
            
        if event == 'Refresh Prices':
            refresh_prices()
            with open(filename, "r") as infile:
                reader = csv.reader(infile)
                header_list = next(reader)
                data = list(reader) 
            window["table"].Update(values=data)

    window.close()

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


def write_dicts_to_csv (dicts):
    """Writes several dictionaries to a CSV file from a list of dictionaries"""
    with open('Wishlist_Program\wishlist.csv', 'w', newline='') as wishlist:
        fieldnames = ['Service','Item_Name','Like_New', 'Excellent', 'Good', 'Well_Used']
        wishlist_writer = csv.DictWriter(wishlist, fieldnames=fieldnames)
        wishlist_writer.writeheader()
        wishlist_writer.writerows(dicts)
    return True

def write_url_to_csv (url):
    '''Writes a URL to a CSV file'''
    service = 'none'
    if search('mpb',url):
        service='MPB'
    elif search('keh',url):
        service ='KEH'

    with open('Wishlist_Program\\urls.csv','a', newline='') as urls:
        writer = csv.writer(urls)
        writer.writerow([len(csv_reader('Wishlist_Program\\urls.csv')),service,url])
    return True

def csv_reader(file):
    '''Takes a CSV file name and opens and reads it into a list then returns that list'''
    csv_list =[]
    with open(file) as kyle:  
        reader = csv.reader(kyle)
        for line in reader:
            csv_list.append(line)
    return csv_list

def url_reader():
    '''This takes the url csv file and reads through the urls and calls the appropriate get info function and returns a list of dictionaries'''
    dicts= []
    urls = csv_reader('Wishlist_Program\\urls.csv')
    for url in urls:
        service = url[1]
        URL = url[2]
        if service == 'MPB': 
            mpb_dict = get_info_mpb(URL)
            dicts.append(mpb_dict)
        elif service == 'KEH':
            keh_dict = get_info_keh(URL)
            dicts.append(keh_dict)
    return dicts

def refresh_prices():
    '''Refreshes Prices in the wishlist csv'''
    dicts = url_reader()
    write_dicts_to_csv(dicts)
    return True



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



if __name__ == "__main__":
    main()