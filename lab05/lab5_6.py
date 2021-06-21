class Transport:
    def __init__(self):
        self.value = 0
        self.speed = 0
        self.year = 0
        self.coord = ""

    def setVal(self, input):
            self.value = input

    def setSpeed(self, input):
            self.speed = input

    def setYear(self, input):
            self.year = input

    def setCoord(self, input):
            self.coord = input

class Car (Transport):
    def __init__(self):
        self.value = 0
        self.speed = 0
        self.year = 0
        self.coord = ""

    def getCarCharacteristics(self):
        print("\nХарактеристики автомобіля\n"
              + "Ціна: " + str(self.value)
              + "\nШвидкість: " + str(self.speed)
              + "\nРік: " + str(self.year)
              + "\nКоординати: " + self.coord)


class Plane (Transport):
    def __init__(self):
        self.value = 0
        self.speed = 0
        self.passengers = 0
        self.coord = ""
        self.year = 0
        self.height = 0

    def setHeight(self, input):
            self.height = input

    def setPassengers(self, input):
            self.passengers = input

    def getPlaneCharacteristics(self):
        print("\nХарактеристика Літака\n"
              + "Ціна: " + str(self.value)
              + "\nШвидкість: " + str(self.speed)
              + "\nРік: " + str(self.year)
              + "\nКоординати: " + self.coord
              + "\nВисота: " + str(self.height)
              + "\nКількість пасажирів: " + str(self.passengers))


class Ship (Plane):
    def __init__(self):
        self.value = 0
        self.speed = 0 
        self.year = 0
        self.port = 0
        self.coord = ""
        self.passangers = 0

    def setPort(self, input):
        if isinstance(input, str):
            self.port = input

    def getShipCharacteristics(self):
        print("\nХарактеристика корабля\n"
              + "Ціна: " + str(self.value)
              + "\nШвидкість: " + str(self.speed)
              + "\nРік: " + str(self.year)
              + "\nКоординати: " + self.coord
              + "\nПорт: " + self.port
              + "\nКількість пасажирів: " + str(self.passengers))


if __name__ == '__main__':
    ship = Ship()
    ship.setVal(250000)
    ship.setSpeed(200)
    ship.setYear(1956)
    ship.setCoord("18:30:245")
    ship.setPassengers(56)
    ship.setPort("Одеський морський порт")
    ship.getShipCharacteristics()
