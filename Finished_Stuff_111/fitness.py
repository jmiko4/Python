''' Hello ladies and gentlemen
Its time for your medicine
Lets find out how healthy you are'''
from datetime import datetime

def main():
    #get the input
    gender = input('What is your gender?(m/f): ')
    birthday = input('What is your birthday?(YYYY-MM-DD): ')
    weight = float(input('What is your weight?(lbs): '))
    height = float(input('What is your height?(inches): '))
    #do some conversions and stuff
    age = compute_age(birthday)
    height_cm = cm_from_in(height)
    weight_kg = kg_from_lb(weight)
    #now lets do some math
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender,weight_kg, height_cm,age)
    print(f'Your BMI is {bmi:.1f} and your BMR is {bmr:.1f}.')

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    kg = pounds/2.20462
    return kg

def cm_from_in(inches):
    return inches*2.54

def body_mass_index(weight, height):
    return (10000*weight)/(height**2)

def basal_metabolic_rate(gender, weight, height, age):
    if gender == 'm':
        return (88.362 + 13.397 * weight + 4.799 * height - 5.677 * age)
    else:
        return (447.593 + 9.247 * weight + 3.098 * height - 4.330 * age)
    

main()