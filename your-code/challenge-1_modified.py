print('Welcome to this calculator! It can add and subtract whole numbers from zero to five')
#FUNCTIONS PART OF THE CODE
#Function input you choose which numbers are going to be added or subtracted (only alphabetical type of characters are allowed)
def number_choose():
    while True:
        number = (input('Choose your number from zero to five: ')).lower()
        
        if number.isalpha and number in ['zero', 'one', 'two', 'three', 'four', 'five']:
            return number

        else:
            print('Sorry I only accept zero, one, two, three, four or five as answer, please try again\n')
#Function input you choose which operator is going to take place(only alphabetical type of characters are allowed)
def operator_choose():
    while True:
        operator = input('What do you want to do? plus or minus: ')
            
        if operator.isalpha and operator in ['plus', 'minus']:
            return operator

        else:
            print('Sorry I only accept minus or plus. \n')

#Dictionary in order to check the values
numbers_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
numbers_dict2 = {0:'zero', 1:'one', 2:'two', 3:'three', 4: 'four', 5: 'five'}

#We are calling the functions we created above.
number_1 = number_choose()

operator = operator_choose()

number_2 = number_choose()

# if statement of the different options of the operator
if operator == 'plus':
    result = numbers_dict[number_1] + numbers_dict[number_2]

elif operator == 'minus' :
    if numbers_dict[number_1] < numbers_dict[number_2]: #If result is negative, I have decided to keep it as 0 (not a negative)
        result == 0
    else:
        result = numbers_dict[number_1]-numbers_dict[number_2]

result2 = numbers_dict2[result]
print(f'{number_1} {operator} {number_1} equals {result2}')