import pylab

import matplotlib.pyplot as plt
letters = list('АБВГҐДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯ')

with open("file.txt") as file:
    text = file.read()
    text = text.upper()
    text = list(text)
    amount = []
    
    for i in range(32):
        amount.append(text.count(letters[i]))
        
    pylab.bar(letters, amount)
    plt.title('Частота появи літер у Заповіті Т.Г. Шевченко')
    plt.savefig('lab_7_2.png', dpi=200)
