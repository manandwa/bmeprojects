# Mobin Anandwala
# Date Created: 9/7/2017
# Purpose: to generate a random name using first hardcoded list and then using a file
# Original code from here: http://liquidthink.net/python-100-program-challenge-program-1-building-simple-name-generator found from google search: random name generator in python
# Updated to include age

import random

# Sampling function
def sample(items):
    randomIndex = random.randrange(len(items))
    return items[randomIndex]

# Ask User for Male, Female or Random name
def promptforGender():
    genderList = ['male','female']
    response = input('What Name Gender would you like? (m/f) (enter r for random): ')
    if response == 'm':
        return 'male'
    elif response == 'f':
        return 'female'
    elif response == 'r':
        return sample(genderList)
    else:
        print('please enter m, f, or r to initiate the Random Name Generator')

def promptforAge():
    ageList = ['14','15','16','17','18']
    print('\t Enter 1 for 14')
    print('\t Enter 2 for 15')
    print('\t Enter 3 for 16')
    print('\t Enter 4 for 17')
    print('\t Enter 5 for 18')
    print('\t Enter 6 for random age')
    response = input('How old would you like your character to be? (Enter 6 for random) ')
    if response == '1':
        return '14'
    elif response == '2':
        return '15'
    elif response == '3':
        return '16'
    elif response == '4':
        return '17'
    elif response == '5':
        return '18'
    elif response == '6':
        return sample(ageList)
    else:
        print('please enter a number 1-6')



# Generate name using lists
def genName():
    # Define list of names
    boyNames = ['Jack', 'Andrew', 'Mike', 'Terry', 'Torvald', 'Gatsby']
    girlNames = ['Alice','Hanna','Clare','Janet','Daisy']
    # ask for gender of name
    gender = promptforGender()
    # ask for age
    age = promptforAge()
    # Generate names based on gender
    if gender == 'male':
        name = sample(boyNames)
    elif gender == 'female':
        name = sample(girlNames)
    # Generate Age
    if age == '14':
        age_out = '14 ' + ' years old'
    elif age == '15':
        age_out =  '15 ' + ' years old'
    elif age == '16':
        age_out =  '16 ' + ' years old'
    elif age == '17':
        age_out =  '17 ' + ' years old'
    elif age == '18':
        age_out =  '18' + ' years old'
    # Final output
    character = 'Your character is named ' + name + ' and is ' + age_out
    return character

# Main program
print('Welcome to the Simple Random Name Generator by Liquid Think!')
print(genName())
