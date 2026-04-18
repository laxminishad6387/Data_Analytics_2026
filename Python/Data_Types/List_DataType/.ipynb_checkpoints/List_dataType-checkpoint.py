# List data type in python(property of list :  1. mutable , 2. allow duplicate values , 3.indexing (index start with 0))

my_List=[10,20,30,40,50] #this is one way to create a list in python
print(my_List) # it will print [10, 20, 30, 40, 50]
print(type(my_List)) # it will print <class 'list'> because my_List is a list variable

my_List2=list((60,70,80,90,100)) #this is another way to create a list using constructor in python
print(my_List2) # it will print [60, 70, 80, 90, 100]
print(type(my_List2)) # it will print <class 'list'> because my_List2 is a list variable


# accessing elements in list data type using indexing and slicing
myList=[10,20,30,40,50,60]
print(myList[0]) # it will print 10 because index 0 value is 10
print(myList[1]) # it will print 20 because index 1 value is 20
print(myList[2]) # it will print 30 because index 2 value is 30
print(myList[3]) # it will print 40 because index 3 value is 40
print(myList[4]) # it will print 50 because index 4 value is 50
print(myList[5]) # it will print 60 because index 5 value is 60
print(myList[0],myList[1],myList[2],myList[3],myList[4],myList[5]) # it will print 10 20 30 40 50 60 because we are printing all index values of myList variable in single print statement
print(myList[-1]) # it will print 60 because index -1 value is 60
print(myList[-2]) # it will print 50 because index -2 value is 50
print(myList[-3]) # it will print 40 because index -3 value is 40
print(myList[-4]) # it will print 30 because index -4 value is 30
print(myList[-5]) # it will print 20 because index -5 value is 20
print(myList[-6]) # it will print 10 because index -6 value is 10
print(myList[:]) # it will print [10, 20, 30, 40, 50, 60] because we are printing all index values of myList variable using slicing operator
print(myList[1:4]) # it will print [20, 30, 40] because we are printing index values from 1 to 3 of myList variable using slicing operator.In list last index is excluded
print(myList[2:]) # it will print [30, 40, 50, 60] because we are printing index values from 2 to end of myList variable using slicing operator. In list last index is excluded
print(myList[:4]) # it will print [10, 20, 30, 40] because we are printing index values from start to 3 of myList variable using slicing operator. In list last index is excluded
print(myList[-4:-1]) # it will print [30, 40, 50] because we are printing index values from -4 to -2 of myList variable using slicing operator. In list last index is excluded
print(myList[-3:]) # it will print [40, 50, 60] because we are printing index values from -3 to end of myList variable using slicing operator.
print(myList[:-2]) # it will print [10, 20, 30, 40] because we are printing index values from start to -3 of myList variable using slicing operator. In list last index is excluded
print(myList[::2]) # it will print [10, 30, 50] because we are printing index values from start to end of myList variable using slicing operator with step 2
print(myList[1::2]) # it will print [20, 40, 60] because we are printing index values from 1 to end of myList variable using slicing operator with step 2
print(myList[::-1]) # it will print [60, 50, 40, 30, 20, 10] because we are printing all index values of myList variable in reverse order using slicing operator with step -1
print(myList[::-2]) # it will print [60, 40, 20] because we are printing all index values of myList variable in reverse order using slicing operator with step -2
print(myList[::3]) # it will print [10, 40] because we are printing index values from start to end of myList variable using slicing operator with step 3



# function in list data type
myList.append(True) # it will append True value to the end of myList variable
print(myList) # it will print [10, 20, 30, 40, 50, 60, True] because we have appended True value to myList variable using append() method

myList.append(90) # it will append 90 value to the end of myList variable
print(myList) # it will print [10, 20, 30, 40, 50, 60, True, 90] because we have appended 90 value to myList variable using append() method. 

myList.insert(3,35) # it will insert 35 value at index 3 of myList variable
print(myList) # it will print [10, 20, 30, 35, 40, 50, 60, True, 90] because we have inserted 35 value at index 3 of myList variable using insert() method. insert method add element at the specified index of list

myList.insert(0,5) # it will insert 5 value at index 0 of myList variable
print(myList) # it will print [5, 10, 20, 30, 35, 40, 50, 60, True, 90] because we have inserted 5 value at index 0 of myList variable using insert() method. insert method add element at the specified index of list
myList.insert(2,["hello", "world"]) # it will insert ["hello", "world"] list at index 2 of myList variable.insert variable only take one index and one value at a time.value can be of any data type like int, string, list, tuple, set, dictionary etc.
print(myList) # it will print [5, 10, ['hello', 'world'], 20, 30, 35, 40, 50, 60, True, 90] because we have inserted ["hello", "world"] list at index 2 of myList variable using insert() method. insert method add element at the specified index of list

myList.extend("hello")
print(myList) # it will print [5, 10, 20, 30, 35, 40, 50, 60, True, 90, 'h', 'e', 'l', 'l', 'o'] because we have extended myList variable with each character of string "hello" using extend() method. extend method add each element of iterable to the end of list
myList.extend(10) # it will give us TypeError like that: TypeError: 'int' object is not iterable because we are trying to extend list with an integer value. extend method only accepts iterable values like list, tuple, string etc.
myList.extend([100,200,300]) # it will extend myList variable with each element of list [100,200,300]
print(myList) # it will print [5, 10, 20, 30, 35, 40, 50, 60, True, 90, 'h', 'e', 'l', 'l', 'o', 100, 200, 300] because we have extended myList variable with each element of list [100,200,300] using extend() method. extend method add each element of iterable to the end of list
myList.extend([-5]) # it will extend myList variable with each element of list [-5]
print(myList) # it will print [5, 10, 20, 30, 35, 40, 50, 60, True, 90, 'h', 'e', 'l', 'l', 'o', 100, 200, 300, -5] because we have extended myList variable with each element of list [-5] using extend() method. extend method add each element of iterable to the end of list
myList.extend([[-4,-3,-2,-1]]) # it will extend myList variable with each element of list [[-4,-3,-2,-1]]
print(myList) # it will print [5, 10, 20, 30, 35, 40, 50, 60, True, 90, 'h', 'e', 'l', 'l', 'o', 100, 200, 300, -5, [-4, -3, -2, -1]] because we have extended myList variable with each element of list [[-4,-3,-2,-1]] using extend() method. extend method add each element of iterable to the end of list

del myList[1] # it will delete index 1 value from myList variable
print(myList) # it will print [5, 20, 30, 35, 40, 50, 60, True, 90, 'h', 'e', 'l', 'l', 'o', 100, 200, 300, -5, [-4, -3, -2, -1]] because we have deleted index 1 value from myList variable using del keyword
del myList[1:4] # it will delete index 1 to 3 values from myList variable
print(myList) # it will print [5, 40, 50, 60, True, 90, 'h', 'e', 'l', 'o', 100, 200, 300, -5, [-4, -3, -2, -1]] because we have deleted index 1 to 3 values from myList variable using del keyword

myList.remove(50) # it will remove 50 value from myList variable.remove method take only one value at a time and remove the first occurrence of that value from the list.it does not take index.
print(myList) # it will print [5, 40, 60, True, 90, 'h', 'e', 'l', 'o', 100, 200, 300, -5, [-4, -3, -2, -1]] because we have removed 50 value from myList variable using remove() method
myList.remove(500) # it will give us ValueError like that: ValueError

myList.pop(-5) # it will remove and return the value at index -5 from myList variable.pop method take only one index at a time and remove the value at that index from the list. if no index is provided it will remove and return the last value of the list.
print(myList) # it will print [5, 40, 60, True, 90, 'h', 'e', 'l', 'o', 100, 200, 300, -5, [-4, -3, -2, -1]] because we have removed the value at index -5 from myList variable using pop() method
myList.pop() # it will remove and return the last value from myList variable
print(myList) # it will print [5, 40, 60, True, 90, 'h', 'e', 'l', 'o', 100, 200, 300, -5] because we have removed the last value from myList variable using pop() method
myList.pop(-100) # it will give us IndexError like that: IndexError: pop index out of range because we are trying to pop value from an index which is not present in the list

mylist2=myList.copy() # it will create a copy of myList variable and assign it to mylist2 variable
print(mylist2) # it will print [5, 40, 60, True, 90, 'h', 'e', 'l', 'o', 100, 200, 300, -5] because mylist2 is a copy of myList variable

mylist2.clear() # it will clear all the values from myList2 variable
print(mylist2) # it will print [] because we have cleared all the values from myList2 variable using clear() method

del mylist2 # it will delete mylist2 variable from memory
print(mylist2) # it will give us NameError like that: NameError: name 'mylist2' is not defined because we have deleted mylist2 variable from memory using del keyword
del mylist2[1]
print(mylist2) # it will give us IndexError: list assignment index out of range

myList.reverse() # it will reverse the order of values in myList variable
print(myList) # it will print [-5, 300, 200, 100, 'o', 'l', 'e', 'h', 90, True, 60, 40, 5] because we have reversed the order of values in myList variable using reverse() method

print(myList.count(40)) # it will print 1 because 40 value is present only one time in myList variable
print(myList.index(200)) # it will print 2 because 200 value is present at index 2 in myList variable.index method return the first occurrence index of the specified value in the list
print(len(myList)) # it will print 13 because myList variable has 13 values in it using len() method
print(sum(myList)) # it will give TypeError: unsupported operand type(s) for +: 'int' and 'str'

myList3=[1,2,3,4,5]
print(sum(myList3)) # it will print 15 because myList3 variable has 5 integer values in it and sum of those values is 15 using sum() method
print(min(myList3)) # it will print 1 because 1 is the minimum value in myList3 variable using min() method
print(max(myList3)) # it will print 5 because 5 is the maximum value in myList3 variable using max() method

