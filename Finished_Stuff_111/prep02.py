import math

num_item = int(input('How many items are you packing?'))
num_box = int(input('How many boxes are you packing?'))

def calculate_items_per_box(num_items, num_boxes):
    
    return num_items/num_boxes

def print_items_per_box():
    print(math.ceil(calculate_items_per_box(num_item, num_box)))

print_items_per_box()



