# EXERCISE 1.1: Simple AND
from importlib.metadata import pass_none

print("\nEXERCISE 1.1: Check if a number is in range")
print("Write a function that returns True if a number is between 1 and 10 (inclusive)")

#def is_in_range(num):
   # """Returns True if num is between 1 and 10 (inclusive)"""
    # TODO: Use AND to check both conditions
    #pass
#num= int(input("Please put in your score?:"))
#if 1<= num <=10:
   # print("True")
#else: print ("False")
#def is_in_range(num):
#    return num>=1 and num<=10
#score= int(input("Are you in range?:"))
#if  is_in_range(score):
#    print(f'You are in Range')
#else:
#    print("Not in Range")


def is_in_range(num):
    return num >= 1 and num <= 10


try:
    # TRY to do the dangerous thing
    score = int(input("Please put in your score (1-10): "))

    if is_in_range(score):
        print("Success! That's in range.")
    else:
        print("Out of range!")

except ValueError:
    # This runs ONLY if the user typed something that isn't a number
    print("Oops! Please enter a whole number, not words or symbols.")

#A Fun Challenge for You (Exercise 1.2)

#Let’s combine everything we've learned: Logic, Short-Circuiting, and Safety.

#Can you write a single if statement that checks if a string is "Safe to Print"?
#A string is "Safe" if:

 #   It is not empty.

  #  It has fewer than 10 characters.

#Hint: Use len(user_input) to check the input
user_input=input("What is your user name?")
if len(user_input)>0 and len( user_input)<10:
    print("Safe to Print.")
else: print("Not Safe To Print.")



