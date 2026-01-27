a="1"
b="2"
print(a+b)
#here in output it will simply add the both strings as for compiler it is string and not int
#to convert it we use funtion that is int()
#python suppport wide range of functions like int(),float(),str(),hex()etc


#here we will type cast the string a and b into integer and add
print(int(a)+int(b))

# Explicit typecasting example
str1="345"
str2="432"
num1=int(str1)
num2=int(str2) # error will be thrown if the string is invalid like not a number but complete alphabates
print("\nThe sum of the str1 and str2 is:",num1+num2)

# Implicit Typecasting example
#in this pytho automatically type cast the variables
a=89    # Python will automatically consider it as int
b=98.99 # Pyhton will automatically consider it as float
print("\nThe type of a is:",type(a))
print("The type of b is:",type(b))
c=a+b # Pyhton will automatically convert the c in to the float as it is a float additionn
print("\nThe sum of a and b is:",c)
print("The type of c is:",type(c))