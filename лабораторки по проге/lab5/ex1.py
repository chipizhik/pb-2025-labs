def convert(a1, b2, c3):
    time = {
        's': 1,
        'm': 60,
        'h': 3600
    }
    sec = a1 * time[b2]
    result = sec / time[c3]
    return result

input_abc = input('введите в формате | 4h m | ')
abc = input_abc.split()
a = int(abc[0][:-1])
b = abc[0][-1].lower()
c = abc[1].lower()
print(str(convert(a, b, c)),c)