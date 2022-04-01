import PySimpleGUI as sg
import csv
from photo_wishlist_scraper import csv_reader, refresh_prices, write_url_to_csv
lists=[]
SERVICE = 0
ITEM_NAME = 1
LIKE_NEW = 2
EXCELLENT = 3
GOOD = 4
WELL_USED=5
# info_lists=csv_reader('Wishlist_Program/wishlist.csv')
sg.theme('Dark Grey 13')
filename = "Wishlist_Program/wishlist.csv"
data = []
header_list = []
with open(filename, "r") as infile:
    reader = csv.reader(infile)
    header_list = next(reader)
    data = list(reader) 
sg.set_options(element_padding=(0, 0))
# layout = []
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
window.close()