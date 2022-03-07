'''Author:H.F.
were gonna do some grade calcualtions with if then else elif or and other stuff
woo hoo'''
import time
import webbrowser


grade = float(input('What is your grade percentage?\n'))

if grade >= 90:
    letter = 'A'
    if grade <= 93:
        letter = 'A-'

elif grade >= 80:
    letter = 'B'
    if grade >= 87:
        letter = 'B+'
    if grade < 83:
        letter = 'B-'

elif grade >=70:
    letter='C'
    if grade >= 77:
        letter = 'C+'
    if grade < 73:
        letter = 'C-'

elif grade >=60:
    letter='D'
    if grade >= 67:
        letter = 'D+'
    if grade < 63:
        letter = 'D-'

elif grade <60:
    letter='F'

if grade>= 70:
    print('Congratulations! You won!')
    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=MoI8Z8Dq1yY')

else:
    print('Oh no! You\'re a failure! (‘◉ ⌓ ◉ ’)')
    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    

print(f'Your letter grade is {letter}.')


