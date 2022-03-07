'''Ok lets talk about life expenctaancy wahooooo
autor: Tu mamá por las dudas'''

import webbrowser
import time

min = 1000000000000000
max = 0
min_name = None
max_name = None
min_year=None
max_year=None
new_year_min = 1000000000000000000
new_year_max = 0
new_year_min_name = None
new_year_max_name = None
new_year_min_year = None
new_year_max_year = None
new_year_avg = 0
new_year_sum = 0
count=0

year= input('What year do you want to learn about?\n')

with open('life-expectancy.csv') as spread_sheet:
    
    for i in spread_sheet:
       
        stripped = i.strip()
        life_list = stripped.split(',')

        if life_list[3] != 'Life expectancy (years)':
            
            if (float(life_list[3])) < min:
                min = float(life_list[3])
                min_name = life_list[0]
                min_year = life_list[2]
                
            if (float(life_list[3])) > max:
                max = float(life_list[3])
                max_name = life_list[0]
                max_year = life_list[2]
        if life_list[2] == year:
           
            if (float(life_list[3])) < new_year_min:
                new_year_min = float(life_list[3])
                new_year_min_name = life_list[0]
                new_year_min_year = life_list[2]
                
            if (float(life_list[3])) > new_year_max:
                new_year_max = float(life_list[3])
                new_year_max_name = life_list[0]
                new_year_max_year = life_list[2]
            
            new_year_sum += float(life_list[3])
            count+=1


print(f'Shortest life expectancy is {min} in {min_name} in {min_year}')
print(f'The longest life expectancy is {max} in {max_name} in {max_year}')


print (f'Let\'s talk about {year}:\n')
if new_year_max != 0:
    print(f'In {new_year_min_year} shortest life expectancy is {new_year_min} in {new_year_min_name}')
    print(f'The longest life expectancy is {new_year_max} in {new_year_max_name} in {new_year_max_year}')
    print(f'The average life expectancy this year is {new_year_sum/count:.2f}')
else:
    print('You didnt enter a valid year')
time.sleep(1)
print('Merry Christmas')
time.sleep(3)
webbrowser.open('https://www.youtube.com/watch?v=euklW45uhsc')

