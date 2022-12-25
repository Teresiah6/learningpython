import os
# with closing file in the event of  a crash
with open("mydata.txt", mode = "w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nsome more random text\nAnd some more")

#open file for reading
with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())
#check if file has closed
print(myFile.closed)
#check filename associated with the file
print(myFile.name)
#check last used mode where r is read
print(myFile.mode)
#rename
os.rename("mydata.txt", "mydata2.txt")
#remove
os.remove("mydata2.txt")
#create directories
#os.mkdir("mydir")
#delete or change a dir
os.chdir("mydir")
#find what current directory is
print("Current dirctory: ", os.getcwd())
#remove a directory but fast move back a dir
os.chdir("..")
#check if you have moved backardsa a dir
print("Current dirctory: ", os.getcwd())
#remove a dir
os.rmdir("mydir")
