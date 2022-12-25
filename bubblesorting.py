import random
import  math

#1. An outer loop decreases in size each time
#2. The goal is to have the largest number at the end of the list when cycle 1 is sone
#3. Inner loop starts comparing indexes a5 the beginning of the loop
#4. check if list[index] > list[index +1]
#5. if so swap the index values
#6. when the inner loop complestes the largest umber is at the end
#7. Decrement the outer loop by 1

numList = []
#5 numbers between 1 and 9
for i in range(5):
    numList.append(random.randrange(1, 10))
print(numList)
#get length of the numlist
i = len(numList) -1 # -1 because it's a zero index
#outer loop / 1st pass?
while i > 1: #numlistis greater than 0
    j = 0

    while j < i:
        print(f"\nIs {numList[j]} > {numList[j + 1]} ")
        # if first num is greater than next swap
        if numList[j] > numList[j + 1]:
            print("Switching taking place")
            #swap
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp

        else:
            print("do not switch")

        j += 1 # continue moving from left to right
        #print list at this point
        for k in numList:
            print(k, end=", ")
        print()
    print("END OF ROUND")

        #decrement i
    i-= 1
#print the result
for k in numList:
    print(k, end= ", ")
#newline
print()


