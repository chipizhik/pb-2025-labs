def prosto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prosto_num(start, end):
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        print("Error!")
        return

    if end < 2 or start > end:
        print("Error!")
        return

    numbers = [str(num) for num in range(max(2, start), end + 1) if prosto(num)]
    print(" ".join(numbers))


data = input('введите: ').split()
if len(data) != 2:
    print("Error!")
else:
    prosto_num(data[0], data[1])
