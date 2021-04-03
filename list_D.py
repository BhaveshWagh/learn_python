"""LIST"""
h = ["hello"]
print(h[0])
print(h[0:1])
# o/p: hello
# o/p: ['hello']
print("--" * 180)

factor = [1, 2, 3, 4, 5]
print(factor[0])
print(factor[0:1])
# o/p: 1
# o/p: [1]

if factor[0] == 1:
    print("True")
else:
    print("False")
# o/p: True
print("--" *180)

"""Nested lists: Means list can contain other lists"""
Nested = [[2, [37]], 4, ["hello"]]

print(Nested)
print(Nested[1])
print(Nested[2][0][3])
print(Nested[0][1:2])

print("--"*180)

# o/p: [[2, [37], 4, ['hello']]
# o/p: 4
# o/p: l
# o/p: [[37]]

"""Updating lists : lists are mutable,unlike strings."""
# Nested = [[2, [37]], 4, ["hello"]]
Nested[0][1][0] = 21
print(Nested)
# o/p: [[2, [21]], 4, ['hello']]
print("--"*180)

List1 = [1, 2, 8, 4, 5]
List2 = List1
List1[2] = 3
print(List1)
print(List2)

"""" what is List2 now ? : List1 & List2 are two names for the same list. 
Therefore the List2 also contain same elements in previous list """

# o/p: List1 = [1, 2, 3, 4, 5]
# o/p: List2 = [1, 2, 3, 4, 5]
print("--" *180)

""" Copying List : A slice of creates a new(sub) list from an old one :
 * Omitting both end points gives a full slice.
  L[:] == L[o:len(1)]
  * To make a copy of a list use a full slice. 
  List2 = List1[:] """

#  List1 = [1, 2, 3, 4, 5]
List2 = List1[:]
List1[2] = 8
print(List1)
print(List2)

 # o/p: List1 = [1, 2, 8, 4, 5]
 # o/p: List2 = [1, 2, 3, 4, 5]

print("--" * 180)

"""Digression on equality"""
List1 = [1, 2, 3, 4, 5]
List2 = [1, 2, 3, 4, 5]
List3 = List1

"""1. list1 & list2 are two lists with same values.
   2. list2 & list3 are two names for same list."""
# if check  List1 == list2.
# if check list1 is list2.

# list1 == list2 is True.
# list2 == list3 is True.

# list1 is list2 is False.
# list2 is list3 is False.

if List1 == List2:
    print("True")
else:
    print("False")
print("--" *180)

if List2 == List3:
    print("True")
else:
    print("False")
print("--"*180)

if List1 is List2:
    print("True")
else:
    print("False")
print("--"*180)

if List2 is List3:
    print("True")
else:
    print("False")
print("--"*180)

""" CONCATENATION : """
List4 = [1, 2, 3, 4]
List5 = [5, 6, 7, 8]
List6 = List4 + List5
print(List6)

print("--"*180)

List7 = [1, 3, 5, 7]
List8 = List7
List7 = List7 + [9]
print(List8)
print(List7)

"""" Note T List7 & List8 are no longer point to same object """
# o/p:List8 = [1, 3, 5, 7]
#o/p:List7  = [1, 3, 5, 7, 9]