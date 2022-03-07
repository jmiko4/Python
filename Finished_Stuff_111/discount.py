'''Author: Justin Mikolajcik
    Purpose : A program that takes a subtotal and returns the discounted total
    Yay functions'''


from datetime import datetime

current_time = datetime.now()
current_day = current_time.weekday()
sub=None

while sub!= 0:

    sub = float((input('What is the subtotal: ')))

    def stretch_01(subtotal,day):
        difference = None
        if day >= 1 and day <= 2 and subtotal < 50:
            difference = 50-subtotal
        return difference


    def get_subtotal(subtotal,day):
        # A function that takes a subtotal and current day and calculates and returns the discounted get_total
        if day >= 1 and day <= 2 and subtotal >= 50:
            subtotal = subtotal*.9
        return subtotal

    def get_tax(subtotal):
        return subtotal*.06

    def get_total():
        return get_subtotal(sub,current_day)+get_tax(sub)

    def print_the_stuff():
        print(f'The subtotal is {get_subtotal(sub,current_day):.2f} The tax amount is {get_tax(sub):.2f} and the total is {get_total():.2f}')


    print_the_stuff()

    print(f'You were {stretch_01(sub,current_day)} dollars away from the discount')

    
    
    



