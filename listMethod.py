num = [5, 2, 1, 7, 4, 5]
num.append(90)
print(num)
num.insert(2, 20)
print(num)
print(num.count(5))
print( 39 in num)
num.sort()
print(num)
num.reverse()
print(num)
copyNum = num.copy() # if case the original list updated, the copied list was not updated
num.append(100)
print(num)
print(copyNum)
num.clear()
print(num)
