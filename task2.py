# Compulsory Task 2

# Prints string to explain program
print ("This program show you which years are leap years.")

# Allows user to enter the two values
year = int(input("What year do you want to start with:"))
numYears = int(input ("How many years do you want to check:"))

# Runs the loop the number of times the user requested
for i in range (1,numYears+1):
    if year%4 == 0: # This is to determine if the year is divisible by 4
        print (str(year) + " is a leap year.") # True this will print
    else: print (str(year) + " is'nt a leap year.") # False this will print
    year += 1 # Adds 1 year onto the starting year
    
