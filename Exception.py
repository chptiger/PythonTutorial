try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Agent cannot be 0')
except ValueError:
    print('Invalid value')
