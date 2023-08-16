#@author Sobomate-Victor Asimiea

import ToDoList as td

class driver:
    print("What would you like to do?\n1.Add a task\n2.Mark as done\n3.View Tasks\n4.Refresh List\n")

    answer = input("Enter Number:\n")
    if answer == 1:
        print(td.addTask())