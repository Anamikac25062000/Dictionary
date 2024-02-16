# 5).Write a Python program to multiply all the items in a dictionary. 


dict = {'Bus': 3, 'Car': 6, 'Jeep': 4, 'Bike': 8 }
multiplication = 1

for num in dict.values():
    multiplication *= num
print(multiplication)
