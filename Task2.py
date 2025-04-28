#Demonstrate List Slicing

numbers = [1,2,3,4,5,6,7,8,9,10]

print("Original list:",numbers)
firstFive = numbers[:5]
print("Extracted first five elements:",firstFive)
firstFive.reverse()
print("Reversed extracted elements:",firstFive)