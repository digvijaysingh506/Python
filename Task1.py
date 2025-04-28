#Create a Dictionary of Student Marks

dictionary = {"Alic":85,"Ram":99,"Rahul":82,"Sujeet":90}
userInput = input("Enter the student's name:")

if userInput in dictionary:
    print(dictionary.get(userInput))
else:
    print("Student not found.")