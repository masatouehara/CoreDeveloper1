#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----


# function of fizzbuzz  
def fizzbuzz(x):
    if x%15 == 0:
        print("Fizzbuzz")
    elif x%5 == 0:
        print("Buzz")
    elif x%3 == 0:
        print("Fizz")
    else:
        print(x)

maxnumber = 100
for i in range(1, maxnumber):
    fizzbuzz(i)


# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----

def calculateCommissionedPay(EmployeeID):
    if EmployeeID == 1:
        return 10
    elif EmployeeID == 2:
            return 20   

def calculateHourlyPay(EmployeeID):
    if EmployeeID == 1:
        return 100
    elif EmployeeID == 2:
        return 200

def calculateSalariedPay(EmployeeID):
    if EmployeeID == 1:
        return 1000
    elif EmployeeID == 2:
        return 2000

def calculatePay(EmployeeID):
    A = calculateCommissionedPay(EmployeeID)
    B = calculateHourlyPay(EmployeeID)
    C = calculateSalariedPay(EmployeeID)
    total = A + B + C
    return total

EmployeeID = 1 //1:TRI-AD or 2:Denso
print("**Check my salary**")
print("My salary is", calculatePay(EmployeeID), "yet")





# -----END PAYROLL CODE-----
