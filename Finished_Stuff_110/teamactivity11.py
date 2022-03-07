'''
team activity
sophia kneedler
HR list
'''



with open("hr_system.txt") as file_hr:
    for line in file_hr:
        strip_hr = line.strip()
        parts = strip_hr.split(" ")
        name = parts[0]
        id = parts[1]
        title = parts[2]
        salary = int(parts[3])
        paycheck = salary/24

        if title.lower() == "engineer":
            paycheck += 1000

        print(f"{name}, (ID: {id}) Title: {title} -- ${paycheck:.2f}")

