#1
listik = [5,2,7,5,2,9,6,3,8,6,]
for i in range(10):
    if listik[i]== 3:
        listik[i] = 30
print(listik)

#2
listik2 = [i for i in range(3,8)]
list2 = [i**2 for i in listik2]
print(listik2, list2)

#3
listik3 = [87,4,9,16,1000]
maxnum = max(listik3)
print(maxnum//(len(listik3)))

#4
kortel1 = (5,322,3.2,322)
if all(isinstance(x, (int, float)) for x in kortel1):
    kortel1 = tuple(sorted(kortel1))
print(kortel1)

#5
pricelist = {'онигири':80,'хлеб':40,'майкаТайсона':99000}
maxpriceitem = max(pricelist, key=pricelist.get)
maxprice = pricelist[maxpriceitem]
minpriceitem = min(pricelist, key=pricelist.get)
minprice = pricelist[minpriceitem]
print('самое дорогое - ', maxpriceitem,' цена -', maxprice)
print('самое дешёвое - ', minpriceitem,' цена -', minprice)

#6
spisok = ['майка', 'тайсона', 5, 'арбуз']
slovar = { subject: subject for subject in spisok }
print(slovar)

#7
RuEnSlovar = {'пиво':'beer',
              'огонь':'fire',
              'копьё':'spear'}
wordRu = input('слово на русском ')
print(RuEnSlovar.get(wordRu))

#8
import random

slark = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']
millionImpacta = {
    'камень': ['ножницы', 'ящерица'],
    'ножницы': ['бумага', 'ящерица'],
    'бумага': ['камень', 'спок'],
    'ящерица': ['бумага', 'спок'],
    'спок': ['камень', 'ножницы']
}
Washvibor = input("Ваш выбор: ").lower().strip()
if Washvibor not in slark:
    print("ты ")
else:
    neWashvibor = random.choice(slark)
    print(f"киборг PICKнул {neWashvibor}")
        
    if Washvibor == neWashvibor:
        print("Ничья")
    elif neWashvibor in millionImpacta[Washvibor]:
        print("победа сил света(я)")
    else:
        print("победа сил тьмя(не я)")