# Loops and Range 
# A loop´is a sequence of instructions continuosly repeated until a specific condition is reached.
# "for loop" is used for iterating over a sequence (than can be any datata structure-list/tuples or even a string )
# Iteration means performing an action repeatedly 

# For example, lets define the following list
# Looping through a List 

print("Looping through a List")
sequence = ["zero", "first","second"]
# Syntax: 
for variable in sequence:
    print(variable)
print("\n")

# Looping thorugh a String 
# Strings are iterable objects, so they contain sequence of characters 
# Example: 
print("Looping through a String")
for i in "apple":
    print(i)
print("\n")

# Another Example 
print("Another Example")
for c in "family":
    print(c.capitalize())
print("\n")

# Enumerate 
# For access to the index of each element of a list 
# The Iterate Function, iterates over the elements of a list and associates an index with them 
# We need to use two variables, to store the values given by enumerate 
# For example: 
print("Enumerate Function")
fam_heights = [1.73, 1.68, 1.50, 1.91]
for index, height in enumerate(fam_heights):
    print("index "+ str(index) + " : "+str(height) )

print("\n")

print("While Loop example")
# While Loop
# Allows to execute a set of statements repeatedly as long as a condition is true 
# Syntax: 
"""
while condition:
    statement(s)
"""
# For example 
x = 1 
while x<4:
    print(x)
    x = x+1 
print("\n")


print("Range Function")
# Range()
# Allows us to generate a series of numbers within a given range
# Allows us to decide where the series of numbers will star and end and how big the difference will be between one number and the next
# The range() function takes three arguments 
# A start argument is starting number of the sequence, the lower limit, by default it starts with 0 if is not specified
# A stop argument is a upper limit, it generates numbers up to this number. The range() doesnt include this number in the result 
# The step is a difference between each number in the result. The default value of the step is one if is not specified 
# The range() function only works with the integers. Not allow to use float number or any other type in a start,
# stop and step argument of the range() function 
# There is three ways for call the range() function 
# range(stop) take only one argument 
# range(start, stop) take two argument 
# range(start, stop, step) takes three arguments 

print("Example: Using only one argument")
# Example using one argument  
print("Print the first 5 numbers using range function")
for i in range(5):
    print(i, end=", ")
print(" \n")
# Use the end argument to print the output in the same line, with a comma separate each value output
# Only a stop argument is passed to range(). So by default, it takes start=0 and step=1 

print("Example: Using two arguments, start=5 and stop=10")
for i in range(5, 10):
    print(i, end=",")
print("\n")

# Example, using three arguments 
# The step value is the difference between each number, is 2 
print("Example, using three arguments start=2, stop=10, step=2")
for i in range(2, 10, 2):
    print(i, end=",")
