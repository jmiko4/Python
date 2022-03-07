'''Autor: Facundito
Voy a escrivir todo este programa en castellano para que los haters no me puedan robar de mi code
Buena po cavro'''
import math

def compute_area(choice):
    if choice == 'square':
        rad = int(input('What is the thing and the stuff?'))
        return esquare(rad)
    elif choice == 'circle':
        rad = int(input('Speak to me dave'))
        return circle(rad)
    elif choice == 'rectangular prism':
        side_one = int(input('Whats side 1'))
        side_one_part_2 = int(input('Whats side 1 part 2'))
        return rectangle(side_one,side_one_part_2)
       

def esquare(radius):
    '''This calculates the square's thing'''
    area = rectangle(radius,radius)
    return area

def circle(radius):
    '''I hate math'''
    area = math.pi * 2*radius
    return area

def rectangle(side_one,side_two):
    '''Y Si veo a tu mamá,
    Yo la pregunta por ti,
    pa ver si ya tenés a alguien,
    alguien que te haga feliz'''
    area = side_one*side_two
    return area

esquare(2)

circle(6)

rectangle(4,8)
choice = input('Yo dawg this is about to get dummy interesting (square or circle)\n')
ans = compute_area(choice)
print(ans)