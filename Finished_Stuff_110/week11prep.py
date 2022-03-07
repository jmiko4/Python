people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
min = 100
max = 0
max_name = None
min_name = None

for i in people:
    name_and_age = i.split()
    if int(name_and_age[1]) >max:
        max = int(name_and_age[1])
        max_name = name_and_age[0]

    if int(name_and_age[1]) <min:
        min = int(name_and_age[1])
        min_name = name_and_age[0]

print (max_name,max, min_name, min)