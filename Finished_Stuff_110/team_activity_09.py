nums = []
num = None
sum = 0
average = 0
biggest = 0
count = 0
smallest = 0

print('Enter a list of numbers, type 0 when finished.')
while num != 0:
    num = int(input('Enter a number: '))
    if num != 0:
        nums.append(num)

for n in nums:
    sum += n

    if n > biggest:
        biggest = n

    if n < smallest and n > 0:
        smallest = n

    count +=1

average = sum/count


print(f'The sum is {sum}')
print(f'The average is {average}')
print(f'The biggest number is {biggest}')
print(f' The smallest positive number is {smallest}')

nums.sort() 
for i in nums:
    print(i)

