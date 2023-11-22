arr = [11, 22, 33, 44, 55]
print("Array is :",arr)
 
res = arr[::-1] #reversing using list slicing
print("Resultant new reversed array:",res)


arr = [11, 22, 33, 44, 55]
print("Before reversal Array is :",arr)
 
arr.reverse() #reversing using reverse()
print("After reversing Array:",arr)


arr = [12, 34, 56, 78]
print("Original Array is :",arr)
#reversing using reversed()
result=list(reversed(arr))
print("Resultant new reversed Array:",result)