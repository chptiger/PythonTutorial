
for item in ['Mosh', 'John','Sarah']:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10): # range from 5 to 10
    print(item)

for item in range(5, 10, 2): # range from 5 to 10, step is 2
    print(item)

prices = [10, 20, 30];
sum = 0
for price in prices: # range from 5 to 10
    sum += price
    print(price)
print(f"Total: {sum}")