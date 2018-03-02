"""
Problem Statement​ ​1:
Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()
Problem Statement​ ​2:
Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()

"""

# Reduce will produce a single result
def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result


# Custom filter function 
def myfilter(anyfunc, sequence):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in sequence:
  if anyfunc(item):
   result.append(item)

 # return funal output
 return result


# test myreduce function
def sum(x,y): return x + y

# test myfilter function
def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True


print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )
print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))

