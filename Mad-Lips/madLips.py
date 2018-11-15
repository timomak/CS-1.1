# Default string for all stories
mad_lips = "Hi {}, your {} has escaped. Use your {} to {} it."

# Heart of the code. Requests and stores user input.
def create_story():
    name = input("Your name: ")
    adjective_first = input("An adgective: ")
    adjective_second = input("An adgective: ")
    verb = input("A verb: ")
    # Prints the default story sentance with user input.
    print(mad_lips.format(name, adjective_first, adjective_second,verb))

create_story()
