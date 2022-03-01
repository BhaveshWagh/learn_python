def is_vowel(str):
    list_of_vowels = ['a', 'e', 'o', 'i', 'u','aeiou']
    if str.lower() in list_of_vowels:
        return True
    else:
        return False



print(is_vowel("a"))
print(is_vowel("aeiou"))




