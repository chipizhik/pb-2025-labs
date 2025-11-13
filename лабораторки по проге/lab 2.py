1
name = input()
age = input()
for i in range(10):
    print(name,age)

2
num2=int(input())
for i in range(2,10):
    print(num2*i)

3
for i in range(0,101,3):
    print(i)

4
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n} равен {factorial}")

5
x= 20
while not(x==0):
    print(x)
    x=x-1

6
limit = int(input('limit '))
fib1 = 1
fib2 = 1
print(fib1)
while fib1<limit:
    fib1= fib1 + fib2
    fib2= fib1 - fib2
    if fib1<limit:
        print(fib1)
    else: break

7
huskar=input('строчка ')
viper=''
for i in range(len(huskar)):
    viper=viper + huskar[i]+ str(i+1)
print(viper)

8
while 1:
    a = int(input ('число 1 '))
    b = int(input ('число 2 '))
    print('сумма',a+b) 
