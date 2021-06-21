import lab04
import pylab
import matplotlib.pyplot as plt


file = "file.txt"

if (lab04.seach_file(file) != None):
       with open(file, mode="r",encoding="utf-8") as f:
           text = f.read()
          
amount = []
sentenses = ["Питальні","Окличні","Звичайні","З трикрапкою"]
amount.append(lab04.how_sentences_in_file_question(file))
amount.append(lab04.how_sentences_in_file_exclamatory(file))
amount.append(lab04.how_sentences_in_file_normal(file))
amount.append(lab04.how_sentences_in_file_three_dots(file))  
     
pylab.bar(sentenses, amount)
plt.title('Частота речень у Заповіті Т.Г. Шевченка')
plt.savefig('lab_7_3.png', dpi=200)

