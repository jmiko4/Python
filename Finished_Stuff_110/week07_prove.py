from PIL import Image

pic1 = Image.open('cat.jpg')
import webbrowser
import time
num = int(input('Pick a number between 1 and 5 to see where our cat will go today\n'))
location = 'beach.jpg'
if num == 1:
    location = 'beach.jpg'
elif num== 2:
    location = 'desert.jpg'
elif num == 3:
    location = 'field.jpg'
elif num == 4:
    location = 'earth.jpg'
else:
    location = 'snowscape.jpg'


pic2 = Image.open(f'{location}')

pixel2 = pic2.load()

# pic1 = pic1.rotate(45)

# pic2 = pic2.rotate(-45)

pixel = pic1.load()

r,g,b = pixel[0,0]

r2,g2,b2 = pixel2[0,0]

width,height = pic1.size

count=0
count1=0


while count < width and count1 < height :

    r,g,b = pixel[count,count1]
    r2,g2,b2 = pixel2[count,count1]

    if r<130 and g>150 and b<110:

        pixel[count,count1] = (r2,g2,b2)
        count = count + 1


        
    else:
        count = count+1

    if count == width:
            count = 0
            count1 =count1 + 1

pic1.save('pic3.jpg')

pic3 = Image.open('pic3.jpg')
pic3.show()
