milage = float (input())
gascost = float (input())



miles20 = 20
miles75 = 75
miles500 = 500




gascost20 = (miles20/milage)* gascost
gascost75 = (miles75/milage)* gascost
gascost500 = (miles500/milage)* gascost

print(f'{gascost20:.2f} {gascost75:.2f} {gascost500:.2f}')
