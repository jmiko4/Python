from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas,scene_width,scene_height)

    draw_ground(canvas,scene_width,scene_height)

    draw_house(canvas,scene_width,scene_height)

    draw_lightning(canvas,scene_width,scene_height)

    draw_clouds(canvas,scene_width,scene_height)

    draw_raindrops(canvas,scene_width,scene_height)





    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="midnight blue")

def draw_ground(canvas,scene_width,scene_height):

    draw_rectangle(canvas,0,0, scene_width,
       scene_height/3,width=0, fill ='dark green')


def draw_house(canvas, scene_width, scene_height):
    #base of house
    draw_rectangle(canvas,350,100,550,250, width=1, fill= 'antique white')
    
    #draw roof
    draw_polygon(canvas, 450, 350,
            600, 250,
            300, 250,
            outline="gray20", width=1, fill="tan4")
    #front door
    draw_rectangle(canvas,450,100,500,200,width=1,fill= 'navajo white')
    draw_oval(canvas,490,140,495,145, width=1, outline="black", fill='white')
    #window
    draw_rectangle(canvas,375,175,425,225,width=1, fill= 'cornflower blue')
    #window pane
    draw_line(canvas, 400, 175, 400, 225, width=5 , fill='navajo white')
    draw_line(canvas, 375, 200, 425, 200, width=5 ,fill='navajo white')
    

def draw_clouds(canvas, scene_width, scene_height):
    '''draws lots of randomly shaped and positioned cloud objects'''
    for i in range(100):
        random_width= random.randint(100,200)
        random_height= random.randint(50,100)
        random_x = random.randint(0,600)
        random_y = random.randint(325,450)
        draw_oval(canvas,random_x, random_y ,random_x + random_width, random_y + random_height ,width=0,outline='black', fill='gray')

def draw_lightning(canvas, scene_width, scene_height):
    '''Draws a single randomly placed and lengthed lightning bolt'''
    random_x = random.randint(0,500)
    random_y = random.randint(0,50)
    draw_line(canvas, 100+random_x,350,150+random_x, 250, width=10, fill='yellow')
    draw_line(canvas, 153+random_x,250,100+random_x,250, width=10, fill='yellow' )
    draw_line(canvas, 100+random_x,250,130+random_x, 130-random_y, width=10, fill='yellow' )

def draw_raindrops(canvas, scene_width, scene_height):
    '''draws 200 randomly placed raindrops'''
    for i in range(200):
        random_x = random.randint(50,720)
        random_y = random.randint(50,325)
        draw_arc(canvas,0+random_x,0+random_y,10+random_x,20+random_y,start=225,extent=90,width=0,fill='royal blue')


main()