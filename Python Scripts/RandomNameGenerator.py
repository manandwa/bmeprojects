# Mobin Anandwala
# Date Created: 9/7/2017
# Purpose: to generate a random name using first hardcoded list and then using a file
# Original code from here: http://liquidthink.net/python-100-program-challenge-program-1-building-simple-name-generator found from google search: random name generator in python

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

# Generate name using lists
def genName():
    # Define list of names
    boyNames = ['Jack', 'Andrew', 'Mike', 'Terry', 'Torvald', 'Gatsby']
    girlNames = ['Alice','Hanna','Clare','Janet','Daisy']
    # ask for gender of name
    gender = promptforGender()
    # Generate names based on gender
    if gender == 'male':
        return sample(boyNames)
    elif gender == 'female':
        return sample(girlNames)

# Main program
print('Welcome to the Simple Random Name Generator by Liquid Think!')
print(genName())
