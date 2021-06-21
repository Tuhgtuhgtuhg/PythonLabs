class ModString (str):

    def __init__(self, input):
            self.s = input

    def substr(self):
        result = False
        s = self.s.lower()

        for i in range(len(s)-3):
            sub = s[i:i+3]
            if sub in s[3:len(s)-1]:
                result = True
                break

        if result:
            return True
        else:
            return False

    def polindrom(self):
        s = self.s.lower()
        if s[::-1] == s:
            return True
        else:
            return False

stroka = ModString("pythonpythonnohtypnohtyp")
print("Введена строка: " + str(stroka))
print("Чи введена строка містить у собі повтори від 3 символів: " + str(stroka.substr()))
print("Чи введена строка є поліндромом: " + str(stroka.polindrom()))


