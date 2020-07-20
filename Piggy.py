# PYTHON LEVEL 1 : Assignment
# -> Save as: Piggy.py
# -> Date due: Monday 13th July 2020

# TASK:
# . Create a python program that is called Piggy, that returns a name based on the starting letter. 
# . If the starting letter is a consonant it adds “ay” to the end after swapping the first letter to the end of the word else it adds “ean” to the end without swapping.

# i.) The input is entered through the keyboard

# FOR EXAMPLE:
# - Safraaz becomes afraazsay
# - Aubemeyang becomes aubemeyangean

# i.) Try different cases i.e Yusuf, Shasaad, Abdulahi, Angel and so on


# -----------------------------------------------------------------------------------

# Input the name 

myName = input("Please type your official first name: \n")

# -----------------------------------------------------------------------------------

# Shifting the first letter of the name inputted to the end of the name

newFirst = myName.lower() #change case to lower --

firstLetter = newFirst[0]

#check the firstletter if vowel or consanant 

if firstLetter in 'aeiou':
    
    #add ean to the name
    newName = newFirst + 'ean'  #angela + ean = angelaean

    print("This is your name scrambled \n")

    print(newName)

else:

    newName = newFirst + firstLetter + 'ay'

    print("This is your name scrambled \n")

    print(newName[1:])

# --------------------------------------------------------------------------------------

# Defining the consonants and vowels



#-----------------------------------------------------------------------------------------------------------------------------













    

 
