class Book:

    def __init__(self, name = " ", year = 0, genre = " "):
        if name != " " and 0<year<=2021 and genre != " ":
            self.name = name
            self.genre = genre
            self.year = year
        else:
            print("Помилка додавання книги!")

class Lib:

    def __init__(self):
        self.library = []

    def addBook(self, Book):
        if Book not in self.library:
            self.library.append(Book)
            print("Книга " + str(Book.name) + " була успішно доданa до бібліотеки")

    def findBook(self, info):
        for search in self.library:
            if search.name == info or search.year == info or search.genre == info:
                print("Книга знайдена!")
                print("Назва: "+str(search.name) + "\nРік: " + str(search.year) + "\nЖанр: " + str(search.genre))
                break
        else:
            print("Книгу не вдаєтся знайти...")

    def delBook(self, b):
        for search in self.library:
            if b is search:
                self.library.remove(b)
                print("Книгу успішно видалено.")

if __name__ == '__main__':
    library = Lib()
    name = input("Введіть назву книги: ")
    year = int(input("Введіть рік редакції книги: "))
    genre = input("Введіть жанр книги: ")
    book = Book(name, year, genre)
    library.addBook(book)
    library.findBook(name)
    library.delBook(book)
    library.findBook(name)
