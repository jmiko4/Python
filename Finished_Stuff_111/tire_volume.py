'''
Author: Justin Mikolajcik   

Purpose:To get an A in the class, and maybe calculate some stuff for a wheel
'''

import math
from datetime import datetime
#some imput stuff and variables
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter= float(input('Enter the diameter of the wheel in inches (ex 15): '))
time=datetime.now()
#cool math
volume = ((math.pi)*(width**2)*aspect*(aspect*width+2540*diameter))/10000000000
#print time
print(f'The approximate volume {volume:.2f} liters')
#Yay conversion
thing=input('Would you like that in fluid ounces?(y/n): ')
if thing == 'y':
    volume_oz = volume*33.814
    print(f'Your volume in fluid ounces is {volume_oz:.2f}')
    with open('volumes.txt', 'at') as volumes_file:
        print (f'Date: {time:%Y-%m-%d}, Width:{width:.2f}, Aspect Ratio: {aspect:.2f}, Diameter: {diameter:.2f}, Volume: {volume:.2f}, Volume(ounces): {volume_oz:.2f}', file=volumes_file)

else:
    with open('volumes.txt', 'at') as volumes_file:
     print (f'Date: {time:%Y-%m-%d}, Width:{width:.2f}, Aspect Ratio: {aspect:.2f}, Diameter: {diameter:.2f}, Volume: {volume:.2f}', file=volumes_file)



