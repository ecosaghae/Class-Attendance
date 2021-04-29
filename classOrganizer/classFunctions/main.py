# This is my functions file!
# Create a dictionary that contains the classes
"""
we need to somewhere to store our classes asw while as the students in them. so dictionaries will be the best to achieve
this result.
we are going to create a dictionary called classes.
Remember The name of the item in the case, 'classes' is referred as the key and
each key is separated by a colon (:) from its values which will be the students. Commas separate all the items
"""
classes = {'Math': ['Efe', 'Uyi'],
           'Science': ['Antonio', 'Nour', 'Efe', 'Nate'],
           'History': ['Efe', 'Nate', 'Uyi']}


# Print out class list
def printclasses():
    print("Here are the following classes:\n")  # \n is to get a new line
    # create a variable and list the classes
    cls_list = list(classes.keys())

    # Print out class list by index the user enters
    for cls in cls_list:
        # This will list out the classes in order we have in our dictionary starting from the index zero
        print(str(cls_list.index(cls)) + ': ' + cls)

    # Print out students


def viewstudents():
    # print out the class by the index number
    cls_list = list(classes.keys())
    printclasses()
    # while true keeping it looping
    while True:
        print("\nPlease type the number of the class you want to list:")
        myclass = input('> ')

        try:
            int(myclass)
        # Print out error message if number is not assigned to class
        except:
            print("That is not a number! Please try again!")
            continue # goes back to the beginning of the while loop

# if the index the user enter is greater or less than zero than our class list then print try again
        if int(myclass) > len(cls_list) or int(myclass) < 0:
            print("That is invalid! Please try again")
# if the index the user enter is greater or greater than the number of our class list then print try again
        elif int(myclass) > len(cls_list) or int(myclass) > 2:
            print("That is invalid! Please try again")

        else:
            print('The following students are in ' + cls_list[int(myclass)] + ":\n")
            for student in classes[cls_list[int(myclass)]]:
                print(student)
            print()
            break  # stops the loop and resumes execution, goes back to the very first while true loop in out main.py


# add student to class
def addstudent():
    cls_list = list(classes.keys())
    printclasses()

    while True:
        print("\nPlease type the number of the class you want to list:")
        myclass = input('> ')

        try:
            int(myclass)
        # Print out error message if number is not assigned to class
        except:
            print("That is not a number! Please try again!")
            continue

        if int(myclass) > len(cls_list) or int(myclass) < 0:
            print("That is invalid! Please try again")

        elif int(myclass) > len(cls_list) or int(myclass) > 2:
            print("That is invalid! Please try again")

        else:
            print('Please type the first name of the student you would like to add:')
            student = input('> ')
            classes[cls_list[int(myclass)]].append(student)  # append is to add or update a value in our dictionary
            print('Student added to class')
            break


# remove student from class
def removestudent():
    cls_list = list(classes.keys())
    printclasses()
    while True:
        print("\nPlease type the number of the class you want to list:")
        myclass = input('> ')

        try:
            int(myclass)
        # Print out error message if number is not assigned to class
        except:
            print("That is not a number! Please try again!")
            # Print out while true statement
            continue

        if int(myclass) > len(cls_list) or int(myclass) < 0:
            print("That is invalid! Please try again")
        elif int(myclass) > len(cls_list) or int(myclass) > 2:
            print("That is invalid! Please try again")

        else:
            student_list = classes[cls_list[int(myclass)]]
            print('The following students are in ' + cls_list[int(myclass)] + ":\n")
            for student in student_list:
                print(str(student_list.index(student)) + ': ' + student)
            print()

            while True:
                print("\nPlease type the number of the student you want to remove:")
                mystudent = input('> ')

                try:
                    int(mystudent)
                except:
                    print("That is not a number! Please try again!")
                    continue

                if int(mystudent) > len(student_list) or int(mystudent) < 0:
                    print("That is invalid! Please try again")
                elif int(myclass) > len(cls_list) or int(myclass) > 2:
                    print("That is invalid! Please try again")

                else:
                    classes[cls_list[int(myclass)]].remove(student_list[int(mystudent)])
                    print("Removed student from class")
                    break
# goes back to our very first while true loop in our main.py
            break
