def my_function(myList, i):
 
    if i == len(myList) - 1 :
        print(myList)
    else:
        for k in range(i, len(myList)):
            myList[i], myList[k] = myList[k], myList[i]  
            print(i , " " , k)         
            my_function(myList, i + 1)   
            print(i , " " , k)       
            myList[i], myList[k] = myList[k], myList[i]
            


myList = ['a', 'b', 'c']
i = 0
my_function(myList, i)

