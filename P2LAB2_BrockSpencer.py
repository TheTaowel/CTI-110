nums = 4
product = 1
average = 0
lstofnums = []

for i in range(nums):
    i = float(input())
    lstofnums.append(i)

for i in lstofnums:

    product = product * i

for i in lstofnums:

    average = average + i

average = average/len(lstofnums)
print(f'{product:.0f} {average:.0f}')
print(f'{product:.3f} {average:.3f}')
