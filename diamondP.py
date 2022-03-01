def p(n):
    for i in range(n):
        print("-"*(n - i - 1),end='')
        print("*-"*(i + 1))
    for j in range(n - 1 , 0 , -1):
        print("-"*(n - j),end='')
        print("*-"*(j))
p(4)


print("*" *180)

def p1(n1):
    for i in range(n1):
        print("-"*(n1 - i)+"-*"*(i + 1))
    for j in range(n1 - 1):
        print("-"*(j  + 2)+"-*"*(n1 - 1 - j))
p1(5)