
#type casting every input() is creating as a string so we need type casting
'''
num1 = input("Enter first number: ")
num2 = input("Enter second Number: ")

sum = int(num1) + int(num2)

print("Sum of number is ", sum)
'''
#This is boring to take int() --> funcition many time in our code so that we need to use below method

num1 = int(input("Enter first number: "))
num2 = int( input("Enter second Number: "))

sum = num1 + num2

print("Sum of number is ", sum)