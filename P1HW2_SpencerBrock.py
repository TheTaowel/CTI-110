# Spencer Brock
# 9/26/2023
# Calculates travel expenses

budget = int(input("Enter Budget: "))

dest = input("Where are you traveling? ")

gas = int(input("Enter gas Budget: "))

food = int(input("Enter food Budget: "))

hotel = int(input("Enter hotel Budget: "))

expenses = gas+food+hotel
print("---------Travel Expenses--------")
print("Location: ", dest)
print("Initial Budget: ", budget)
print()
print("Gas Cost: ", gas)
print("Gas Food: ", food)
print("Gas Hotel: ", hotel)
print()
print("remaining Balance: ", budget-expenses)
           
