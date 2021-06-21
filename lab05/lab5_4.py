import random

class Card:

    def __init__(self):
        self.mast = random.choice(["Чирва", "Піка", "Трефа", "Бубна"])
        self.num = random.choice([6, 7, 8, 9, 10, "Валет", "Дама", "Kороль", "Туз"])

    def show(self):
        print("Масть: " + self.mast + "\n" + "Ціна: " + str(self.num))

class Stack:

    def __init__(self):
        self.stack = []
        for i in range(35):
            random_card = Card()
            if random_card not in self.stack:
                self.stack.append(random_card)

    def findByIndex(self, index):
        if 0<=index<=35:
            print(str(index) + " картка зі стопки : "  )
            self.stack[index].show()
        else:
            print("Індекс вийшов за межі діапазону")

    def showStack(self):
        for index in range(35):
            self.stack[index].show()

    def getSixCards(self):
        for i in range(6):
            random.choice(self.stack).show()

    def transport(self):
        new = random.sample(self.stack,len(self.stack))
        for elem in new:
            elem.show()

if __name__ == '__main__':
    A = Stack()
    A.showStack() 
    print()
    A.findByIndex(12) 
    
    print("\nШість випадкових карт\n")
    A.getSixCards()
    
    print("\n! Нова колода !\n")
    A.transport()
