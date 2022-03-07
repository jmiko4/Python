import pandas as pd
import math

def main():
    cans=[]
    with open('tin cans.csv') as file:
        for line in file:
            line = line.strip()
            split_line = line.split(',')
            cans.append(split_line)

    for can in cans:
        radius = float(can[1])
        height = float(can[2])
        volume= compute_volume(radius, height)
        surface = compute_surface_area(radius, height)

        print(f' Yo dawg yur volume is {volume} and your surface area is {surface} and this is for {can[0]} and probably is {compute_efficiency(volume,surface)} close quote')



    
    
    
    

def compute_volume(radius,height):
    return math.pi*(radius**2)*height

def compute_surface_area(radius,height):
    return 2*math.pi*radius*(radius+height)

def compute_efficiency(volume,surface):
    '''this class is a meme'''
    return volume/surface

main()