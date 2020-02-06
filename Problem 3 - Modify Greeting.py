# Problem 3 – Modify the previous program such that only the users you and your instructor are greeted with their names
# Created by Kamil Krawczyk
# 02/02/2020

name = input("What is your name? - ")
# asks user about name
if name == "Kamil":
 print("Hello Kamil");
# if input is "Kamil" it will welcome user
elif name == "Laleh":
  print("Hello professor");
# if input is "Laleh" it will welcome professor
else: 
  print("Sorry not a confirmed user");
# if input is anything else it will not welcome user