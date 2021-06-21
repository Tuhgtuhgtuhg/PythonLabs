class Dictionary:
    def __init__(self):
        self.dictionary = dict()

    def addWordTranslate(self, word, translation):
        if word != "" or translation != "":
            if word not in self.dictionary.keys():
                self.dictionary[word] = translation
                print("Слово \"" + word + "\" було успішно додано до словника")
            else:
                print("Слово вже існує у словнику!")
        else:
            print("Помилка додавання слова до словника!")

    def showTranslation(self, word):
        if word in self.dictionary.keys():
            print("Переклади для слова \"" + word + '\":')
            print(self.dictionary[word])
        else:
            print("Помилка, слова \"" + word + "\" немає у словнику!")

if __name__ == '__main__':
    Dict = Dictionary()
    Dict.addWordTranslate("doll", ["гарненька дитина", "дівчина", "коханка", "лялька"])
    Dict.addWordTranslate("doll", "дол")
    Dict.addWordTranslate("brother", "Брат")
    Dict.showTranslation("brother")
    Dict.showTranslation("doll")
    Dict.showTranslation("Egor")
