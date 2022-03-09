'''
This is going to be crazy!
This program will make a dictionary with stuff in it!
'''

def main():

    dict = read_dict('students.csv')
    user_i_number = input('Please enter an i-number: ')
    if user_i_number in dict.keys():
        print(f'This i-number belongs to {dict[user_i_number]}')
    else:
        print(f'This i-number is not in the dictionary')

def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dict ={}
    with open(filename) as csvfile:
        next(csvfile)
        for line in csvfile:
            split = line.split(',')
            dict[split[0]] = split[1]
    
    return dict


main()