#Read a File and Handle Errors
fileName= "sample.txt"
i =0
try:
    inputFile = open(fileName,"r")

    print("Reading file content:")
    for line in inputFile:
        i+=1
        print("Line",i,": ",line)
    inputFile.close()
except FileNotFoundError:
    print("Error : The file",fileName,"was not found.")

