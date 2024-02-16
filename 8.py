# 8).Create a function that takes a string and returns a dictionary where keys are letters, and values are the number of times each letter appears in the string  


def letters(input_string):
    num_of_letters = {}
    
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            num_of_letters[char] = num_of_letters.get(char, 0) + 1
    
    return num_of_letters

str = "Anamika at Beinex"
result = letters(str)

print(result)
