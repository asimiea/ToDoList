#@author Sobomate-Victor Asimiea

import ToDoList as td

class driver:
    while True:
        print("What would you like to do?\n1.Add a task\n2.Mark as done\n3.View Tasks\n4.Refresh List\n5. Exit")

        answer = int(input("Enter Number:\n"))
        if answer == 1:
            td.addTask()
        elif answer == 2:
            td.removeTask()
        elif answer == 3:
            td.printList()
        elif answer == 4:
            td.clear()
        elif answer == 5:
            break
        else:
            print("Please enter a valid option\n")
            