
def miles_per_gallon(starting_od, ending_od, gal):
    mpg = (ending_od - starting_od) / gal
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = (235.215/mpg)
    return lp100k

def main():
    user_starting_od = float(input('What is the starting odometer: '))
    user_ending_od = float(input('What is the ending odometer: '))
    user_gal = float(input('How many gallons of gas did you use: '))
    calc_mpg = miles_per_gallon(user_starting_od, user_ending_od,user_gal)
    calc_lp100k = lp100k_from_mpg(calc_mpg)
    print(f'{calc_mpg}, {calc_lp100k}')

main()



