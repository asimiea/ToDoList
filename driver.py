#@author Sobomate-Victor Asimiea

import ToDoList as td

class driver:
    entries = []
    
    while True:
        print("\nWhat would you like to do?\n1. Add a task\n2. Mark as done\n3. View List\n4. Refresh List\n5. Exit")

        answer = int(input("Enter Number: "))
        if answer == 1:
            td.addTask(entries)
        elif answer == 2:
            td.removeTask(entries)
        elif answer == 3:
            td.printList(entries)
        elif answer == 4:
            td.clear(entries)
        elif answer == 5:
            break
        else:
            print("Please enter a valid option\n")
            