# Problem 5 - Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.
#Created by Kamil Krawczyk
#02/02/2020

miles_driven = float(input("How many miles have you driven? - "));
# asks the user to input how many miles driven
gallons = float(input("How many gallons have you used? - "))
# asks the user to input how many gallons were used
calc_mpg = (miles_driven / gallons);
# MPG calculation
print("Your MPG is", calc_mpg)
#prints the results to the user