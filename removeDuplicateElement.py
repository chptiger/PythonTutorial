nums = [1, 4, 1, 2]
uniques = []
for num in nums:
    if num not in uniques:
        uniques.append(num)
print(uniques)