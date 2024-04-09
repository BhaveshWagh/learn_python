def check_case(ch):
    if ch.isupper():
        return 'U'
    elif ch.islower():
        return 'L'
    else:
        return 'Invalid input'

# Take user input
ch = input()

# Check and print the result
result = check_case(ch)
print(result)
