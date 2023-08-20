#@author Sobomate-Victor Asimiea

def addTask(entries):
    entry = input("Enter a new task: ")
    entries.append({"task": entry, "status": "pending"})
    #print("adding Task")

def removeTask(entries):
    entry_number = int(input("Enter the number of the entry you want to mark as completed: ")) - 1

    if 0 <= entry_number < len(entries):
        entries[entry_number]["status"] = "completed"
        print("Task marked as completed!")
    else:
        print("Invalid entry number.")

def printList(entries):
    print("TO DO List:")
    for idx, entry in enumerate(entries, start=1):
        print(f"{idx}. [{entry['status']}] {entry['task']}")
    #print("printing List")

def clear(entries):
    entries.clear()
    print("List refreshed")