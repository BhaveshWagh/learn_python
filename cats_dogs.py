filenames = ['textfiles\cats.txt', 'textfiles\dogs.txt']
for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        print("This file has not found.")