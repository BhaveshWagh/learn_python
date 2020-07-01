print("Are u quite then type 'Quite'")
filename = 'textfiles\guest_book.txt'
while True:
    name = input("Enter your name :")
    if name == 'quit':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(name + "\n")
        print(f"hello Mr.{name}, u have been added to the guest list")
