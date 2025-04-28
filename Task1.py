#Calculate Factorial Using a Function

number = int(input("Enter a number: "))

def factorial(number):
    if(number<2):
        return 1
    else:
        return number*(factorial(number-1))

print("factorial of ", number," is : ",factorial(number))