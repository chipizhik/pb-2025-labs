n, m = map(int, input("Введите размер матрицы (строки столбцы): ").split())


if n < 2 or m < 2:
    print("Ошибка: матрица должна быть 2x2 или больше")
    exit()

print(f"\nВведите первую матрицу {n}x{m} (построчно, числа через пробел):")
matrix1 = []
for i in range(n):
    row = list(map(float, input(f"Строка {i+1}: ").split()))
    if len(row) != m:
        print(f"Ошибка: в строке должно быть {m} чисел")
        exit()
    matrix1.append(row)

print(f"\nВведите вторую матрицу {n}x{m} (построчно, числа через пробел):")
matrix2 = []
for i in range(n):
    row = list(map(float, input(f"Строка {i+1}: ").split()))
    if len(row) != m:
        print(f"Ошибка: в строке должно быть {m} чисел")
        exit()
    matrix2.append(row)


result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)


print("\nРезультат сложения матриц:")
for row in result:
    print(" ".join(f"{num:g}" for num in row))