'''Author: Edgar Allen Poe
Alright brothers and sisters lets do some coding
Amén Hermano Amén'''

with open('hr_system.txt') as hr_info:
    # hr_list = list(hr_info)
    for i in hr_info:
        stripped = i.strip()
        hr_list = stripped.split()
        cool_math= float(hr_list[3])/12
        if hr_list[2] == 'Engineer':
            cool_math+=1000
        print(f'{hr_list[0]} (ID: {hr_list[1]}), {hr_list[2]} - ${cool_math:.2f}')
    # for i in hr_list:
    #     print(i.strip())