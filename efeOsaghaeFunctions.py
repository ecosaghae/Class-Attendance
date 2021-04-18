# INF360 - Programming in Python
# Efe Osaghae
# Final

# This is my functions file!

# Create a dictionary that contains the classes
classes = {'History': ['Efe', 'Antonio'],
           'Math': ['Efe'],
           'Science': ['Nate']
           }


# Print out class list
def printclasses():
    print("Here are the following classes:\n")

    cls_list = list(classes.keys())

    # Print out class list by index the user enters
    for cls in cls_list:
        print(str(cls_list.index(cls)) + ': ' + cls)


# Print out students 
def viewstudents():
    cls_list = list(classes.keys())
    printclasses()
    # print out the class by the index number
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

        else:
            print('The following students are in ' + cls_list[int(myclass)] + ":\n")
            for student in classes[cls_list[int(myclass)]]:
                print(student)
            print()
            break


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

        else:
            print('Please type the first name of the student you would like to add:')
            student = input('> ')
            classes[cls_list[int(myclass)]].append(student)
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

        else:
            stu_list = classes[cls_list[int(myclass)]]
            print('The following students are in ' + cls_list[int(myclass)] + ":\n")
            for student in stu_list:
                print(str(stu_list.index(student)) + ': ' + student)
            print()

            while True:
                print("\nPlease type the number of the student you want to remove:")
                mystudent = input('> ')

                try:
                    int(mystudent)
                except:
                    print("That is not a number! Please try again!")
                    continue

                if int(mystudent) > len(stu_list) or int(mystudent) < 0:
                    print("That is invalid! Please try again")

                else:
                    classes[cls_list[int(myclass)]].remove(stu_list[int(mystudent)])
                    print("Removed student from class")
                    break

            break
