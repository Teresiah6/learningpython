#create a file named my #mydata2.txt - I already had it
#use what you learned in part 8 and find out how to open a file without using with
#Open inside of a try block
#catch a FileNotFoundError
#in ele print contents of the file
#in finally - print message
#open non-existent file mydata3.txt
try:
    #open file without using with
    myFile = open("mydata3.txt", encoding="utf-8")
#as is used to access methods and data in the exception class
except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)
else:
    print("File: ", myFile.read())
    #close file since it was not opned with 'with'
    myFile.close()
finally:
    print("Finsihed working with file")