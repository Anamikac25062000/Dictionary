# 2).Write a Python program to get dictionary keys as a list 


def list1(input_dict):
    new_list = list(input_dict.keys())
    return new_list

dict = {'Name': "Anamika", 'Age': 23, 'Company': 'Beinex'}

result = list1(dict)

print(result)
