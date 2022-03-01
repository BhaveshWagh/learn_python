for i in range(1, 6):
    for j in range(5, i, -1):
        print(".",end="")
    for k in range(0, i):
        print(i, end="")
    print()

print("--" * 90)

dot = 4
for i in range (1, 6):
    #  for j in range(1, i + 1):
    print("." * dot , i ,sep='')
    dot -=  1

print("--" * 90)

def number_loops(num):
    for i in range(1, num + 1):
        print("." * (num - i) , "*" * i,sep='')
print(number_loops(5))


print("....1")
print('...22')
print('..333')
print('.4444')
print('55555')