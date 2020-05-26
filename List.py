names = ['John', 'Bob', 'Thomas']
print(names)
print(names[2])
print(names[-1]) # the last element of the list
print(names[1:2]) # the index from 1, not include 2
print(names[1:])

nums = [3, 6, 2, 8, 4]
max = nums[0]
for item in nums:
    if item > max:
        max = item
print(f'Max: {max}')