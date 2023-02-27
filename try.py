def count_vowels(str):
    result = len(list(filter(lambda x : (x == "a"),str)))
    return result

str = ["as","ssd","as"]
print(count_vowels(str))    