add_names = True
while add_names:
    name = input("Please enter you name: ")
    print("Hello, " + name)
    filename = 'guest_book.txt'
    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")
    adding = input("Do you want to quit? (yes/no)")
    if adding == 'yes':
        add_names = False