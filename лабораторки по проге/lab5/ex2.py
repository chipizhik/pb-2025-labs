def Razvod(a, n):
    sumPercent = min(5, a // 10000 * 0.3)

    curAmount = a
    for year in range(1, n + 1):
        if year <= 3:
            termPercent = 3
        elif year <= 6:
            termPercent = 5
        else:
            termPercent = 2

        ablosutPercent = sumPercent + termPercent
        curAmount *= 1 + ablosutPercent / 100

    return round(curAmount - a, 2)

print(Razvod(30000, 3))
print(Razvod(100000, 5))
print(Razvod(200000, 8))
