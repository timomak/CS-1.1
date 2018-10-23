checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    update(index, ("√" + read(index)))

def select(function_code):
    if function_code == "A":
        new_item = input("Add to list:")
        if type(new_item) is str:
            create(new_item)
        # else select("A")

    # Read item
    elif function_code == "R":
        item_index = user_num_input("Index Number to remove: ")
        destroy(item_index)
        # Remember that item_index must actually exist or our program will crash.

    elif function_code == "U":
        item_index = user_num_input("Index Number you'd like to update: ")
        new_item = input("New item name: ")
        update(item_index, new_item)

    elif function_code == "C":
        items_index = user_num_input("Completed item: ")
        print(item_index)
        mark_completed(items_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def user_num_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = int(input(prompt))
    return user_input

running = True
while running == True:
    selection = input("A to add to list\nR to Remove from list\nU to update item\nC to complete item\nP to display list\nQ to exit.\nInput: ")
    print("Selection: ", selection)
    if selection == "Q" or selection == "q":
        running = False
    else:
        select(selection.upper())

def test():
    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

# test()
