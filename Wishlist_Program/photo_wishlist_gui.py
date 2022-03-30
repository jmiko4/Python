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
info_lists=csv_reader('Wishlist_Program/wishlist.csv')
sg.theme('DarkAmber')

layout = [  [sg.Text('Welcome to the Wishlist Program, Add a KEH or MPB url')],
            [sg.Text('URL'), sg.InputText(do_not_clear=False)],
            [sg.Button('Add Item URL'), sg.Button('Refresh Prices')] ]
# Create the Window
window = sg.Window('Wishlist', layout)
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