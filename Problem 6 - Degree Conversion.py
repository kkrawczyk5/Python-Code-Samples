
# Problem 6 - Write a program that will convert degrees Fahrenheit to degrees Celsius.
# Created by Kamil Krawczyk
# 02/02/2020

get_fah = float(input("Input the Fahrenheit degree that you would like to be converted to Celsius - "))
# asks user for the input
calc_c = ((get_fah - 32) * 5/9);
# calculates the conversion
print("That converted to Celsius is - ", calc_c)
# print out the converted answer