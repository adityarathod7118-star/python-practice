a ="Aditya"
print("Hello,",a)
# anything we write between the single or double quot in python is considered as string
#if we want to print the double quot in the string we have to use the single quot 
print('He said,"I want to eat an apple".')


# For multi line string we can use the triple single quot or triple double quot
a='''This is an example of the multiple line string 
We can write it in diff lines and it will be printed as it is when enclosed in the triple single quot
also , We can use triple double quot.'''
print(a)
b="""Heyy
He said,
'I want to eat an apple'."""
print(b)

# Accessing characters of a String
# This is done by using square brackets and writing the index inside it the index starts with 0
x="Lion"
print(x[0])
print(x[1])
print(x[2])
print(x[3])
# print(x[4]) # This will throw an error

# Looping through strings
# the syntax is : for character in name of string:
#                  print(character) 
for character in x:
    print(character)

# Loop in the multiple line string.
    y='''Now we will take a example of multi-line string
    and loo through it and see the output'''
    for character in y:
        print(character)  

# Determining the length of the string
Name="Aditya Rathod"
z=len(Name)
print("The string Name is,",z,"letters long")

#String as an array
print(x[0:1]) # This means it will prent the character up to 0 index and the 11st index won't be printed
print(x[:3]) # We can even skip writing the zero , python will automatically consider it as zero
print(x[3])

# if want the string to be printed from 2 to 6 index
g="Congratuations"
print(g[1:7]) 

# Negative slicing of string
print(g[:-3]) 
# the pyhton interprites it as print(g[0:len(g)-3]) len of string minus 3 which equals to 14-3=11 
# so it will be like print(g[0:11]) it will print till the index number 10

print(g[-3:-1]) 
# Now how the python interprits it print(g[len(g)-3:len(g)-1])
# This means that print(g[14-3:14-1])====print(g[11:13]) means it will print from iindex 11 to 13