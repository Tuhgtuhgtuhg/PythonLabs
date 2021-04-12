from math import floor
while True:
    n = input("Введіть натуральне число n для обчислення формули у = 2*4*6*…*(2*n): ")
    try:
        n = int(n)
        if (n <= 0) :
            print("""Нажаль число n повинно бути  натуральним !!! 
Спробуйте ще раз!""")
        else:
            break
    except ValueError:
            print("""Введенні данні не являються цілим числом !!! 
Спробуйте ще раз!""")
            
y = 1
for i in range(1,n+1):
    y=y*i*2

print( "y = " + str(y))
