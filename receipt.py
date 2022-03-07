'''
This is gonna be some gnarly code that will make a receipt
Author: Justin Mikolajcik All Rights Reserved
'''

def main():
    Name=0
    Price=1
    Quantity = 1
    '''Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
Prints the products_dict.
Opens the request.csv file for reading.
Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
Use the requested product number to find the corresponding item in the products_dict.
Print the product name, requested quantity, and product price.'''
    product_dict = read_dict('products.csv', 0)
    print(product_dict)
    with open('request.csv') as file:
        next(file)
        for line in file:
            split = line.split(',')
            product_stuff = product_dict[split[0]]
            name = product_stuff[Name].strip()
            price = product_stuff[Price].strip()
            quantity = split[Quantity].strip()
            print(f'{ name }, { price }, { quantity }')




def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dict ={}
    with open(filename) as file:
        next(file)
        for line in file:
            split = line.split(',')
            dict[split[key_column_index]]=[split[1],split[2]]

    return dict

if __name__ == "__main__":
    main()