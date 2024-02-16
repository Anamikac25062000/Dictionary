# 3).Write a Python program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys 


dict = {num: num**2 for num in range(1, 16)}
print(dict)
