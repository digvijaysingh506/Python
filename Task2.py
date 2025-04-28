#Write and Append Data to a File

fileName="sample.txt"

inputData = input("Enter text to write to the file:")
with open(fileName, "w") as file:
    file.write(inputData+"\n")
    print("Data successfully written to", fileName)
    file.close()

print()
inputData = input("Enter additional text to append:")
with open(fileName, "a") as file:
    file.write(inputData)
    print("Data successfully appended")
    file.close()

print()
print("Final contents of", fileName)
with open(fileName, "r") as file:
    for line in file:
        print(line)