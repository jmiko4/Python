'''Wahoo'''
import webbrowser
import time
temp = None
chill = None
type = None

temp = float(input('What is the temperature?\n'))
type = input('Fahrenheit or Celsius (F/C)?\n')
if type.lower() == 'c':
    temp = (temp * 9/5) + 32

def windchill(temp):
    '''This function is gonna be supa crazy cool and calculate windchill and print a ton of stuff'''
    wind = 5
    while wind < 61:
        chill = 35.74 + (0.6215*temp) - 35.75*(wind**0.16) + (0.4275*temp*(wind**0.16))
        print(f'At temperature {temp:.1f}F, and wind speed {wind} mph, the windchill is: {chill:.2f}f')
        wind += 5

windchill(temp)

time.sleep(4)
webbrowser.open('https://www.xmasclock.com/')