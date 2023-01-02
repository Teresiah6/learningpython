'''
,list comprehension make it easier to work with multidimensional lists
'''
multiList = [[1,2,3],
             [4,5,6],
             [7,8,9]]
#middle column
print([col[1] for col in multiList])
#diagonal -1 5 9
print([multiList[i][i] for i in range(len(multiList))])