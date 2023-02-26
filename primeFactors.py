def primeFactors(n):
    inc = 2
    base = n
    factorArr = []
    factorDict = {}
    for i in range(1, n):
        if base % inc == 0:
            factorArr.append(inc)
            base = base // inc
        else:
            inc += 1

    string = ''

    for i in range(len(factorArr)):
        if factorArr[i] in factorDict:
            factorDict[factorArr[i]] += 1
        else:
            factorDict[factorArr[i]] = 1

    for factor in factorDict:
        string += f"{factor} ^ {factorDict[factor]} * "

    return string[0: len(string) - 3]


print(primeFactors(20580))
