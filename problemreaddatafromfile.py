#ccyel through each line, output num of words and average word length
import os
with open ("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:
        line = myFile.readline()
        if not line:
            break
        #print line
        print("Line", lineNum)

            #split()
        wordList = line.split()

            #len() to find number of words\
        print("Number of Words : ", len(wordList))

            #loop and count no. of chars in words in list
        charCount = 0
        for word in wordList:
            for char in word:
                charCount+=1

            #find average length of each
            #div char count / len word list
        avnumchar = charCount/len(wordList)

        print(f"Average word length: {avnumchar:.2f}")

        lineNum += 1