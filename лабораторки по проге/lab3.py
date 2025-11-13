# 1
tempC = int(input('температура '))
if tempC>=20:
    print('кондиционер включен')
else:
    print('кондиционер выключен') 

#2
month = int(input('номер месяца '))
if 1<=month<=3:
    print('зима')
if 4<=month<=6:
    print('весна')
if 7<=month<=9:
    print('лето')    
else:
    print('осень')

#3

try:
    x= int(input('возраст собаки по людски '))
    if x==0:
        print(f'собаке {x} лет по собачьи')
    elif x==1 or x==2:
        a= x * 10.5
        print(f'собаке {a} лет по собачьи')    
    elif x>2:
        a=  (2 * 10.5)+ (x-2)*4
        print(f'собаке {a} лет по собачьи') 
    elif x>22:
        print('ошибка')
    elif x<1:
        print('ошибка')
except ValueError:
    print('ошибка')

#4
numb=int(input('число '))
if (numb % 2 ==0 )and (sum(map(int, str(numb)))% 3 ==0):
    print('делится')
else: print('не делится')

#5
password=input('придумайте пароль ')
a1=[str(i)for i in 'qwertyuioplkjhgfdsazxcvbnm']
a2=[str(i)for i in 'QWERTYUIOPLKJHGFDSAZXCVBNM']
a3=[str(i)for i in '!@#$%^&*()_+-=~`[]}{<>.,/?']
a4=[str(i)for i in '1234567890']
a1if = False
a2if = False
a3if = False
a4if = False
lenif = False
if (len(password)>=8):
    lenif = True
if (any(hero in password for hero in a1)):
    a1if = True
if (any(hero in password for hero in a2)):
    a2if = True
if (any(hero in password for hero in a3)):
    a3if = True
if (any(hero in password for hero in a4)):
    a4if = True
if a1if and  a2if and a4if and a3if and lenif:
    print('пароль крутой')
if not(lenif):
    print('пароль короткий')
if not(a1if):
    print('нету строчных букв')
if not(a2if):
    print('нету нету заглавных букв')
if not(a3if):
    print('нету спец символов')
if not(a4if):
    print('нету цифр')