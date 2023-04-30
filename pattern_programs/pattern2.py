# 1
# 12
# 123
# 1234
# 123
# 12
# 1


for i in range(1,6):
    for j in range(1,i):
        print(j,end="")
    print()
for i in range(1,6):
    for j in range(1,5-i):
        print(j,end="")
    print()