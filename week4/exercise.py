#!/usr/bin/env python

# Week 4 Exercises: Comments and Formatting

# EXERCISE 1:

# The function below is an implementation of bubble sort
# Rewrite it with proper comments and formatting using Clean Code standards

#Function: Bubble sort

# maximum numer go to right side
def MaxnumberGotoRight(x):
    n = len(x)
    for i in range(0,n-1):
        if x[i] > x[i+1]:
            x[i] , x[i+1] = x[i+1] , x[i]
    return x

def bubblesort(x):
    n = len(x)
    for i in range(n,1,-1):  
        MaxnumberGotoRight(x)
        #print(i,":",x)
    return x

#TEST
x = [22,20,1,5,6,13,4,0,1]
print(bubblesort(x))

# EXERCISE 2:

# Create a Python function that find the number of instances of a substring
# within a string. For example given the string "abcda" and the substring "a"
# the function should return 2
# Write a proper multiline docstring for your code

# - - - - Enter code here or in separate file - - - -

def Substring(word,substring):
    n = len(word)
    count = 0
    for i in range(n):
        if word[i] == substring:
            count += 1
    return count

word = "abdsa"
substring = "b"
print(Substring(word,substring)) #output the number
