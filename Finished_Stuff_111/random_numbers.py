import random
def main():
    numbers = [16.2, 75.1, 52.3]
    print (numbers)
    append_random_numbers(numbers, 4)
    print(numbers)

def append_random_numbers(numbers,quantity=1):

    for _ in range(quantity):
        numbers.append(round(random.uniform(0,100), 1))

main()