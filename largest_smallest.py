""" Write a function named smallest_largest that asks the user to enter numbers,
 then prints the smallest and largest of all the numbers typed in by the user.
 You may assume the user enters a valid number greater than 0 for the number of numbers to read.
 Here is an example dialogue:"""

# How many numbers do you want to enter? 4
# Number 1: 5
# Number 2: 11
# Number 3: -2
# Number 4: 3
# Smallest = -2
# Largest = 11



def smallest_largest():
    total_numbers = int(input("How many numbers do you want to enter? "))
    list = []
    i = 1
    while i <= total_numbers:
        num = int(input(f"Number {i}: "))
        list.append(num)
        i = i + 1
    print("Smallest =",min(list))
    print("Lagest =",max(list))

print(smallest_largest())
print("# "*100)


# list = []
# num = int(input("enter no"))
# for i in range(num):
#     numbers = int(input("enter element"))
#     list.append(numbers)
# print(min(list),max(list))

#
#
# list2 = []
# num1 = int(input("enter nno"))
# for i in range(num1):
#     numbers2 = int(input("enter elements"))
#     list2.append(numbers2)
#     list2.sort()
# print("smallest emlement",list2[0])
# print("largest element",list2[-1])

