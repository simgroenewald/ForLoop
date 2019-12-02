# Compulsory Task 1

# Variable for user to choose number they would like the times table of.
num = int(input("Enter the number you would like to see the times table of:"))
print ("The " + str(num) + " times table is:")

# for loop which will run 12 times:
for i in range (1,13):
    answer = num * i
    print (str(num) + " x " + str(i) + " = " + str(answer))
