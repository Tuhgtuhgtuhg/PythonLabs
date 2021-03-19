from math import floor
import random
while True:
    N = float(input("Введіть кількість елементів у масиві : "))
    if (N > 0 and N == floor(N)):
        N = int(N)
        break
    else: 
        print("""Нажаль кількість елементів у масиві  повинно позначатися цілим числом та більшим за 0 !!! 
Спробуйте ще раз!""")
array = []
sumPairedElem = 0
countPairedElem = 0
for i in range(N):
    array.append(random.randint(-N,N))
    if (int(array[i])%2==0):
        sumPairedElem = sumPairedElem + array[i]
        countPairedElem = countPairedElem + 1
print("Створений масив: \n"+ str(array))
print("Найменшим елементом у масиві є число " + str(min(array)))
print("Середнє арифметичне парних елементів масиву: "+ str(sumPairedElem/countPairedElem))
print("Ненульові елементи  у зворотному порядку: \n" + str(list(filter(lambda num: num != 0, reversed(array)))))

