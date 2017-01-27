# Mobin Anandwala
# 1/11/12016
# This code will do the following
# Roll four six sided dice
# Order them from largest to smallest
# Discard the smallest one
# Add the result of the remaining values
# Display the result

import random

min = 1
max = 6
dice_value = []

start_roll = 1

while start_roll == 1:
	dice_value = [random.randint(min,max)]
	dice_value.append(random.randint(min,max))
	dice_value.append(random.randint(min,max))
	dice_value.append(random.randint(min,max))
	start_roll = 0

#print(dice_value)

dice_sort = sorted(dice_value,reverse=True)
print(dice_sort)
#print('The lowest value is ' + str(dice_sort[3]))
dice_sort.pop(3)
#print('The values left are ' + str(dice_sort))
final_value = sum(dice_sort)
print('Your ability score is: ' + str(final_value))

