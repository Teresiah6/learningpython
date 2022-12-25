import os
with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\n And some more")
with open("mydata2.txt", encoding="utf-8") as myFile:
# to help keep track of line numbers read
    lineNum = 1
    while True:
        line = myFile.readline()

        if not line:
            break
        print("line", lineNum, " : ", line, end="")
        lineNum += 1

