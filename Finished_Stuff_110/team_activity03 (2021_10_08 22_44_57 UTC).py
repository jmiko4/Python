'''
Author: JUSTIN MIKOLAJCIK   
THIS IS SOME FANCY CODE
BE PREPARED TO SEE MATH DONE
'''
import math
side = float(input("What is the length of a side of the square in cm? \n"))
square = side**2
quickmaths = square/10000
print(f'The area of the square is {square}cm² or {quickmaths}m²')

length = float(input('What is the length of rectangle in cm?\n'))
width = float(input('What is the width of rectangle in cm?\n'))
rec= length*width
quickmaths2 = rec/10000
print(f'The area of the rectangle is {rec}cm² or {quickmaths2}m²')

radius = float(input('What is the radius of the circle in cm?\n'))
circle = (math.pi* (radius**2))
quickmaths3 = circle/10000
print (f'The area of the circle is: {circle}cm² or {quickmaths3}m²')

#lets get crazy
thing = float(input('Give me a length in cm I DARE YOU\n'))
squarething = thing**2
circlething = (math.pi*(squarething))
cube = thing**3
sphere = (thing**3)*4/3*math.pi

print(f'So you didnt ask, but here is the area of the square if that length was the side of a square: {squarething}cm² or {squarething/1000}m²')
print(f'And if it was the radius of a circle the area would be {circlething}cm² or {circlething/10000}m²')
print(f'And finally if it was the side of a cube it would be {cube}cm³ or {cube/10000}m³')
print(f'Si fuera un sphere seria {sphere}cm³ or {sphere/10000}m³')