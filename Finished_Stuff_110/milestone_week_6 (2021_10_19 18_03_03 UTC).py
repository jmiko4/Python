import time
import webbrowser

print('You’re walking in the woods')
time.sleep(2)
print('No one is around and your phone is dead')
time.sleep(2)
print('Out of the corner of your eye you spot some movement')
time.sleep(2)

print('What do you do?')
time.sleep(.5)
print('RUN')
time.sleep(.5)
print('FREEZE')
time.sleep(.5)
print('GET CLOSER')
ans1 = input().lower()

if ans1 == 'run':
    print('You begin to walk, then jog then you break into a sprint.')
    time.sleep(2)
    print('After a while you look behind and you realize whatever is following you is gaining on you.')


elif ans1 =='freeze':
    print('You stand as still as you can. You hope that if it’s some sort of predator that it won’t see you.' 
    'You couldn’t tell how big it was from the initial movement you saw, but you’d rather not know just in case it is a bear or some sort of large animal. '
    'After a little while you decide the coast is clear and continue your walk back to your car. You just can’t quite remember where that was.' 
    'It’s so easy to get turned around in woods like these. You spot a cabin in the woods.')

elif ans1 == 'get closer':
    print('You slowly get closer. You stop. It’s a man. He seems familiar, but you can only see him from behind')