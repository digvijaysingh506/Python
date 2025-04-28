#Check and print number is odd or even

userInput = input("Enter a number: ")

if(int(userInput)>0 and int(userInput)%2==0):
    print(userInput," is an even number")
else:
    print(userInput," is an odd number")