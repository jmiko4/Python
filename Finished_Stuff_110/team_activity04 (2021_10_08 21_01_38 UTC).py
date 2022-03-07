'''Author:ME
I am so excited
Science rules'''
import math
#We are now gonna ask them for the variables and store them
print('Welcome to the velocity calculator program. When promted, enter the variable requested\n')

choice = int(input('Choose which object we are going to calculate the velocity of.\nPress 1 for bowling ball\nPress 2 for loaf of bread\nPress 3 for skydiver\nPress 4 for your own object.'))

if choice == 1:
    mass = float(input('Mass (in kg): '))
    gravity = float(input('Gravity(in m/s², 9.8 for Earth, 24 for Jupiter): '))
    time = float(input('Time (in seconds): '))
    density = float(input('Density of the fluid (in kg/m³, 1.3 for air, 1000 for water): '))
    area= float(input('What is the Radius of Bowling Ball'))
    drag = .5

if choice == 2:
    mass = float(input('Mass (in kg): '))
    gravity = float(input('Gravity(in m/s², 9.8 for Earth, 24 for Jupiter): '))
    time = float(input('Time (in seconds): '))
    density = float(input('Density of the fluid (in kg/m³, 1.3 for air, 1000 for water): '))
    area= float(input('What is the Radius of your mighty loaf'))
    drag = 1.1

if choice == 3:
    mass = float(input('Mass (in kg): '))
    gravity = float(input('Gravity(in m/s², 9.8 for Earth, 24 for Jupiter): '))
    time = float(input('Time (in seconds): '))
    density = float(input('Density of the fluid (in kg/m³, 1.3 for air, 1000 for water): '))
    area = 1.9
    drag = float(input('Drag constant (0.7 for feet first, 1.0 for horizontal): '))

if choice == 4:
    mass = float(input('Mass (in kg): '))
    gravity = float(input('Gravity(in m/s², 9.8 for Earth, 24 for Jupiter): '))
    time = float(input('Time (in seconds): '))
    density = float(input('Density of the fluid (in kg/m³, 1.3 for air, 1000 for water): '))
    area = float(input('Cross sectional area (in m²): '))
    drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))   

#Here is the math

c = ((1/2)* density*area*drag)
velocity = (math.sqrt((mass*gravity)/c))*(1-math.exp(-((math.sqrt(mass*gravity*c)/mass)*time)))
#Lets tell em what is going on
print(f'\nThe inner value of c is: {c:.3f}')
print(f'The velocity after {time} seconds is: {velocity:.3f} m/s')

#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
