# Simple input function 
a=input("Enter a number:")
print(a)

# Whatever we enter in the input functio it is enterd in the form of string 
# So in order to perform operation we have to first perform the typecasting 
x=input("Enter the first number: ")
y=input("Enter the second number: ")
sum=(int(x)+int(y))
print("The sum of the x and y is:",sum)

z=input("Enetr the third number:")
sum1=(int(x)+float(z))
print("The sum of x and z is:",sum1)
