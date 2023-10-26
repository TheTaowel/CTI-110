#CTI-110
#P3HW2-Salary
#spencer Brock
#10/26/2023



name = input("employee name: ")
hours = float(input("employee hours: "))
payrate = float(input("employee payrate: "))
pay = hours * payrate
overtime = 0 
overpay = 0

if hours >= 40:
    overtime = hours - 40
    overpay = overtime * (payrate * 1.5)
    pay = (hours - overtime) * payrate
grosspay = overpay + pay

print("Employee name:", name)
print("Hours worked:", hours)
print("Pay Rate:", payrate)
print("OverTime:", overtime)
print("OverTime Pay:", overpay)
print("RegHour Pay:", pay)
print("Gross Pay:", grosspay)
 
