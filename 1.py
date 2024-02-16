#1).Write a Python program to merge two Python dictionaries. 


def merge(dictionary1, dictionary2):
    merged_dict = dictionary1.copy()
    merged_dict.update(dictionary2)
    return merged_dict

dict1 = {"Name": "Anamika", 'Age': 23}
dict2 = {"Place": "Kasaragod", "Company":"Beinex"}
result = merge(dict1, dict2)

print(result)
