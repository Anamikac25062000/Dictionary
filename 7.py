# 7).Write a Python program to Delete a list of keys from a dictionary 


dict = {'Name': 'Anamika', 'Age': 23, 'Place': 'Kasaragod', 'Company': 'Beinex'}
delete_list = ['Age', 'Place']

for key in delete_list:
    dict.pop(key, None)
print("New Dictionary:", dict)
