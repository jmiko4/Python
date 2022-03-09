'''
This is gonna be some gnarly code that will make a receipt
Author: Justin Mikolajcik All Rights Reserved
'''
import datetime
import time
print('Hi welcome to walmart!')
time.sleep(1)
input('Please choose your character\nMom   Student   Stray Dog\n')
time.sleep(1)
print('*You shop for a while*')
time.sleep(1)
print('*Now you\'re waiting in line*')
time.sleep(1)
print('*You scan and bag your groceries*')
time.sleep(1)
choice= input('Walmart NPC: Would you like your receipt?(y/n)')
if choice == 'y':
    time.sleep(1)
    def main():
        Name=0
        Price=1
        Quantity = 1
        subtotal = 0
        total_quantity = 0
        '''Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
    Prints the products_dict.
    Opens the request.csv file for reading.
    Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
    Use the requested product number to find the corresponding item in the products_dict.
    Print the product name, requested quantity, and product price.'''
        try:
            product_dict = read_dict('products.csv', 0)
            print("Walmart\n")
            with open('request.csv') as file:
                next(file)
                for line in file:
                    split = line.split(',')
                    product_stuff = product_dict[split[0]]
                    name = product_stuff[Name].strip()
                    price = product_stuff[Price].strip()
                    quantity = split[Quantity].strip()
                    print(f'{ name }:{ quantity } @ ${ price }')
                    subtotal = subtotal + (float(price)*int(quantity))
                    total_quantity = float(quantity)+total_quantity
            print(f"\nTotal quantity:{total_quantity:.0f}")
            print(f'Subtotal:{ subtotal:.2f}')
            tax = subtotal*.06
            print(f'Tax:{tax:.2f}')
            total = subtotal + tax
            print(f'Total:{total:.2f}')
            print('Thank you for shopping with us')
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except FileNotFoundError as not_found_err:
            print(not_found_err)
            print('Please choose a different file')
        except PermissionError as perm_err:
            print(perm_err)
            print('Please choose a different file')
        except KeyError as key_err:
            print('Please choose a different key, that one doesnt exist')




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
else:
    print('Thanks for shopping at walmart')