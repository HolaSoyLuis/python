def getValues(number):
    values = []
    for i in range(1, number):
        if number % i == 0:
            values.append(number / i)
    return values

print(getValues(60))
