"""
1. View all the students
2. Add students to class
3. Remove students from classes
4. Exit the program
"""
# Import sys provides functions and variables which are used to manipulate different parts of the Python Runtime
# Environment. It lets us access system-specific parameters and functions
'''
Whenever we call import logging it actually go to this package that comes with python. It saying all the functions 
that are here 'website', make it accessible in our script so we can call these functions.
so for example, in order to track an event or tell us something is wrong, we use 'logging.warning()'
'''
import logging

# we are going to have a seperate file for our functions

from classFunctions.main import viewstudents, addstudent, removestudent

'''
To display the date and time of an event, place '%(asctime)s %(message)s' 
this will tell us the date and time this event was logged
'''
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')

# Let user know classFunctions is found
try:
    from classFunctions import *
    logging.debug("classFunctions.py imported successfully!")
except:
    logging.critical("classFunctions.py is missing! Program will now exit!")
    print("classFunctions.py is missing! Program will now exit!")
    exit()

# Print out if import function found
''' 
while true means loop forever. The while statement takes an expression and excutes the loop body while the expression
evaluates to (boolean) "true". 
So as long as the condition is true, the condition will run indefinitely until something with the loop returns or breaks
'''
while True:
    print('Welcome to my class organizer!')
    print('*' * 50)
    print('1. View students in classes')
    print('2. Add students to classes')
    print('3. Remove students from classes')
    print('4. Exit the program')

# '\n' makes a new line
    print('\nPick a number from above: ')
    choice = input('> ')

    # Print out students
    if choice == '1':
        # view students
        viewstudents()
    elif choice == '2':
        addstudent()
    elif choice == '3':
        removestudent()
    elif choice == '4':
        print('Thank you for using my program!')
        exit()
    else:
        print("That is not a valid number!")
