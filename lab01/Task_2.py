from math import floor
while True:
    n = float(input("Введіть натуральне число n для обчислення формули у = 2*4*6*…*(2*n): "))
    if (n > 0 and n == floor(n)):
        n = int(n)
        break
    else: 
        print("""Нажаль число n повинно бути цілим та більшим за 0 !!! 
Спробуйте ще раз!""")
y = 1
for i in range(1,n+1):
    y=y*i*2

print( "y = " + str(y))
