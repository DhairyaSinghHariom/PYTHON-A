# Input 
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")


usertext = input("What is your name? ")
print("Hello", usertext)

# How to add 2 numbers entered on Python?
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# How to find the Average of 2 Entered Numbers on Python?
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

average =(int(num1) + int(num2))

print('average:{0} '.format(average))



# How to calculate the Entered Visa and Final Grade Average on Python?

visa = float(input("Enter visa grade: "))
final = float(input("Enter final grade: "))

average = visa * 0.3 + final * 0.7

print("Average:", average)
