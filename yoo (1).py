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
def is_in_range(num):
    return num>=1 and num<=10
score= int(input("Are you in range?:"))
if  is_in_range(score):
    print(f'You are in Range')
else:
    print("Not in Range")