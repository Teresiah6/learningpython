#Get the number of rows for the tree and convert to integer
tree_height = eval(input("How tall is the tree: "))
#Get the starting spaces for rthe top of the tree
spaces = tree_height - 1
#There is one hash to start that will be incremented
hashes = 1
#save the stump spaces till later
stump_spaces = tree_height - 1
#make sure the right number of rows are printed
while tree_height != 0:
    #print the spaces
    for i in range(spaces):
        print(' ', end="")
#print the hashes
    for i in range(hashes):
        print('#', end="")
#newline after each row is printed
    print()
#Decrement the spaces by 1 every time
    spaces-=1
#increment hashes by 2
    hashes+=2
#Decrement tree height each time to jump out of the loop
    tree_height -=1
#print the spaces before the stump and then the hash
for i in range(stump_spaces):
    print(' ', end="")
print("#")