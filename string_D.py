""" STRING: Strings are immutable(not change)   """
""" string is a sequence or list of charecters : 0, 1, 2..... ,n-1 """
myqoute =  ''' "Hitchheker's" '''
STR = "Mayur"
print(STR[3])
print(STR[-1])
#o/p: 'u'
#o/p: 'r'

print(myqoute)
#o/p:"Hitchheker's"

print(type(myqoute))
#o/p: < class 'str'>

print("--" * 180)

""" Extracting substrings : A slice is a "segment" of a string."""
""" Eg : string[i:j]"""

string = "Hello"
print(string[0:1])
print(string[0:2])
print(string[3:1])
print(string[1:2])
print(string[:])
print(string[1:])
print(string[0:len(string)])
print("__" *190)

#O/p: H
#O/p: He
#O/p: ' '
#O/p: e
#O/p: Hello
#O/p: ello

""" Concatenation "+" operator : combine two strings -"""

Con = "Hello "
C   = "World!"
t   = Con + "MR. kapil"
print(t)
combine = Con + C
print(combine)

#o/p: Hello MR. kapil
#o/p: Hello World!

""" Length : It defines length of string  """
print(len(Con))
#o/p: 6