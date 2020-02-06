  # Problem 4 - Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.
# Created by Kamil Krawczyk
# 02/02/2020

radius = float(input("What is the radius of the circle? - "))
# asks the user to input the radius of the circle
radius_calc = ((3.14 * (radius ** 2)));
# equation to calculate the area of the circle
print("The area of the circle is", radius_calc)
# Prints out the radius of the circle
