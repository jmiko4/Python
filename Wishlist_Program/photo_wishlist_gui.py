import PySimpleGUI as sg
import csv
from photo_wishlist_scraper import csv_reader
lists=[]
SERVICE = 0
ITEM_NAME = 1
LIKE_NEW = 2
EXCELLENT = 3
GOOD = 4
WELL_USED=5
info_lists=csv_reader('Wishlist_Program/wishlist.csv')
sg.theme('DarkAmber')

layout = [  [sg.Text('Welcome to the Wishlist Program, Add a KEH or MPB URL')],
            [sg.Text('URL'), sg.InputText()],
            [sg.Button('Add Item URL'), sg.Button('Remove Item')] ,
            [sg.Text(f'{info_lists[1][SERVICE]}: {info_lists[1][ITEM_NAME]}- Like New: {info_lists[1][LIKE_NEW]} Excellent: {info_lists[1][EXCELLENT]} Good: {info_lists[1][GOOD]} Well Used: {info_lists[1][WELL_USED]}')]]

# Create the Window
window = sg.Window('Wishlist', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()