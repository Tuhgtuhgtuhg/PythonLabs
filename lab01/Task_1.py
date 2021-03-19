from math import sqrt

while True:
    m = float(input("Введіть число m для обчислення формули z=sqrt((m+3)/(m-3)): "))
    if (m<=-3 or m > 3):
        break
    else: 
        print("""Нажаль число m повинно лежати у такому проміжку: m ∈ (-∞;-3]U(3;∞) !!! 
Спробуйте ще раз!""")
z = sqrt((m+3)/(m-3))
if (z == -0.0 or z == 0.0 ):
    z = 0
print( "z = " + str(z))
