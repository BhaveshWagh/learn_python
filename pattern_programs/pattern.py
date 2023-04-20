# Print the following pattern
# 12345
# 12345
# 12345
# 12345
# 12345
for i in range(5):
    for j in range(1,6):
        print(j,end="")
    print()

print("-*-*-" * 25)

# Print the following pattern
# 1
# 22
# 333
# 4444
# 55555
for i in range(1, 6):
    for j in range(i):
        print(i,end="")
    print()

