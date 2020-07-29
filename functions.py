#Create new file 
#Save as functions.py
#Save in Python-Level-2 folder  --- repo(repository)

#add two numbers

def AddNumbers(x, y, z):   #definition of the function

    return x + y + z

def GetSquares(x):

    return x * x


#call our function

Total = AddNumbers(4,9,100)

#output the results

print(f"The sum total is = {Total}")

#Ask the user for inputs from the keyboard

num1 = int(input("Enter any number \n"))

num2 = int(input("Enter another number \n"))

num3 = int(input("Enter another number again \n"))

#Call the function once again

sum = AddNumbers(num1,num2, num3)

#Print the sum

print("the sum now of {0} plus {1} plus {2} is equal {3}".format(num1, num2, num3, sum))

#call the squares function

print(GetSquares(4))

square = GetSquares(16)


print("the square is ", square)

#A function that calculates the area of Circle

def AreaOfCircle(r):  #pi
    PI = 3.142  #declared a constant --- whose values don't change --- static -- uppercase

    return (PI * r ** 2)



#function call

area = AreaOfCircle(14)

#display the results

print("The area is =",area)


#function definition 

def AreaOfRectangle(): #No parameters

    l = eval(input("Enter the value for the length of your rectangle \n"))  #prompt user for the length
    w = eval(input("Enter the value for the width of your reactangle \n"))  #prompt user for width

    Area = l * w

    print("Area of rectangle is ",Area)

#function call
 

AreaOfRectangle()


#Exercise write a function to calculate the perimeter of rectangle  

#Push you code online


















