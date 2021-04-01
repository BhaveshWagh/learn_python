""" Anagram means : An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
                    Eg. earth = heart """

def Anagram(s1, s2):
    if len(s1) != len(s2):  # short circuit
        return False
    tlist = list(s2)
    i = 0
    while i < len(s1):
        j = 0
        found = False
        while j < len(tlist) and not found:
            if s1[i] == tlist[j]:
                found = True
            else:
                j += 1
        if not found:
            return False
        else:
            i += 1
            tlist[j] = None
    return True

print(Anagram("heart", "earth"))
print(Anagram("hearth", "earth"))
""" Output :  True
              False """

print("-" * 180)

def Anagram_1(s3, s4):
    print(f"s3 = {s3}")
    print(f"s4 = {s4}")

    if len(s3) != len(s4):
        return False # short circuit

    l3 = list(s3)
    l4 = list(s4)
    print(f"l3 = {l3}")
    print(f"l4 = {l4}")

    l3.sort()
    l4.sort()

    print(f"l3 = {l3}")
    print(f"l4 = {l4}")

    for i in range(0,len(s3)): # n
        if l3[i] != l4[i]:
            return False
    return True

print(Anagram_1("heart", "earth"))
print(Anagram_1("python", "typhon"))
print(Anagram_1("python", "typhoe"))

"""  Output :
            s3 = heart
            s4 = earth
            l3 = ['h', 'e', 'a', 'r', 't']
            l4 = ['e', 'a', 'r', 't', 'h']
            l3 = ['a', 'e', 'h', 'r', 't']
            l4 = ['a', 'e', 'h', 'r', 't']
            True
            
            s3 = python
            s4 = typhon
            l3 = ['p', 'y', 't', 'h', 'o', 'n']
            l4 = ['t', 'y', 'p', 'h', 'o', 'n']
            l3 = ['h', 'n', 'o', 'p', 't', 'y']
            l4 = ['h', 'n', 'o', 'p', 't', 'y']
            True
            
            s3 = python
            s4 = typhoe
            l3 = ['p', 'y', 't', 'h', 'o', 'n']
            l4 = ['t', 'y', 'p', 'h', 'o', 'e']
            l3 = ['h', 'n', 'o', 'p', 't', 'y']
            l4 = ['e', 'h', 'o', 'p', 't', 'y']
            False """