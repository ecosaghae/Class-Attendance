# INF360 - Programming in Python
# Efe Osaghae
# Final Project

# 1. List all the students in the classes
# 2. Add students in the classes
# 3. Remove students from classes
# 4. Exit the program

import sys
import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')

# Let user know efeOsaghaeFunctions is
try:
    from efeOsaghaeFunctions import *

    logging.debug("Functions imported successfully!")
except:
    logging.critical("efeOsaghaeFunctions.py is missing! Program will now exit!")
    print("efeOsaghaeFunctions.py is missing! Program will now exit!")
    sys.exit()

# Print out if import function found
while True:
    print('Welcome to my class organizer!')
    print('*' * 50)
    print('1. View students in classes')
    print('2. Add students to classes')
    print('3. Remove students from classes')
    print('4. Exit the program')

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
        sys.exit()
    else:
        print("That is not a valid number!")
