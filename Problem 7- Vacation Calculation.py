# Problem 7 - It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
# Created by Kamil Krawczyk
# 02/02/2020

starting_day = int(input("With Sunday being 0 and Saturday being 6, what day of the week did you leave? - "))
# asks the user to input which day of the week left
vacation_length = int(input("How many days did your vacation last? - "))
# asks the user how long the vacation lasted
comeback_day = (starting_day + vacation_length) % 7
# equation for which day of the week the user came back
print("You will come back on day -", comeback_day)
#outputs the answer
