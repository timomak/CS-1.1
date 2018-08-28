# TODO: Get the Update and mark completed working! Add colored text in terminal.
checklist = list()
completed = list()
running = True

def create(item):
    checklist.append(item)
    completed.append(0)

def read(index):
    item = checklist[index]
    print(checklist[index])
    return item

def update(index, item):
    if isinstance(index, int):
        checklist[index] = item
        completed[index] = 0
    else:
        print("Error: Invalid input.")
        return


def destroy(index):
    if isinstance(index, int):
        checklist.pop(index)
        complted.pop(index)
    else:
        print("Error: Invalid input.")
        return

def list_all_items():
    index = 0
    for list_item in checklist:
        if completed[index] == 0:
            print("[ ] " + "{} {} ".format(index, list_item))
        elif completed[index] == 1:
            print("[V] " + "{} {} ".format(index, list_item))
        index += 1
def mark_completed(index):
    complted.pop(index)
    completed.insert(index, 1)


    print(completed[index])

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    newUser_input = input(prompt)
    return str(newUser_input)

def user_numInput(prompt):
    newUser_input = input(prompt)
    if isinstance(newUser_input, str):
        return "Please use numbers"
    return int(newUser_input)

def select(function_code):
    # Create item
    if function_code == "A":
        new_item = user_input("Add to list:")
        if type(new_item) is str:
            create(new_item)
        # else select("A")

    # Read item
    elif function_code == "R":
        item_index = user_numInput("Index Number to remove: ")
        destroy(item_index)
        # Remember that item_index must actually exist or our program will crash.

    elif function_code == "U":
        item_index = user_numInput("Index Number you'd like to update: ")
        new_item = user_input("New item name: ")
        update(item_index, new_item)

    elif function_code == "C":
        items_index = user_numInput("Completed item: ")
        mark_completed(items_index)
    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

while running == True:
    selection = user_input("A to add to list\nR to Remove from list\nU to update item\nC to complete item\nP to display list\nQ to exit.\n")
    if selection == "Q" or selection == "q":
        running = False
    else:
        select(selection.upper())
# def test():
#     # Your testing code here
#     create("purple sox")
#     create("red cloak")
#     list_all_items()
#     print (completed)
#     #
#     # print(read(0))
#     # print(read(1))
#     #
#     # update(0, "purple socks")
#     #
#     # destroy(1)
#     #
#     # print(read(0))
#     #
#     # mark_completed(0)
#     # list_all_items()
#     # Call your new function with the appropriate value
#     select("C")
#     # View the results
#     # list_all_items()
#     # Call function with new value
#     # select("R")
#     # # View results
#     # list_all_items()
#     # Continue until all code is run
#     # select("P")
#     # list_all_items()
#     # select("Q")
# test()
