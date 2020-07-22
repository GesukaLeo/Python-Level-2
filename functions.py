#Create new file 
#Save as functions.py
#Save in Python-Level-2 folder  --- repo(repository)

#add two numbers

def AddNumbers(x,y):   #definition of the function

    return x + y

def GetSquares(x):

    return x * x


#call our function

Total = AddNumbers(4,9)

#output the results

print(f"The sum total is = {Total}")

#Ask the user for inputs from the keyboard

num1 = int(input("Enter any number \n"))

num2 = int(input("Enter another number \n"))

#Call the function once again

sum = AddNumbers(num1,num2)

#Print the sum

print("the sum now of {0} plus {1} is equal {2}".format(num1, num2, sum))

#call the squares function

print(GetSquares(4))








