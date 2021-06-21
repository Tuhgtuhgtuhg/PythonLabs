import random 

class Student:

    def __init__(self, name, **dictionary):
        if isinstance(dictionary["max_marks_ind"], int) and isinstance(dictionary["max_marks_lab"], int):
            if dictionary["count_labs"] and dictionary["marks_for_passing"]:
                self.name = name
                self.max_marks_i = dictionary["max_marks_ind"]

                self.max_marks_l = dictionary["max_marks_lab"]

                self.count_labs = dictionary["count_labs"]

                self.marks_part = dictionary["marks_for_passing"]


                self.marks_for_labs = []
                self.mark_for_ind = 0
                print("Студент " + name + " був успішно створений!")
            else:
                print("Помилка створення студента!")
        else:
            print("Помилка створення студента!")

    def get_tries_lab(self, try_pass, mark):
        if int(mark) < int(self.max_marks_l) and self.max_marks_l != None:
            for i in range(int(self.count_labs)):
                passed_try = random.randint(int(0), int(try_pass))
                if passed_try >= 1:
                    self.marks_for_labs.append(random.randint(int(mark), int(self.max_marks_l)))
                else:
                    self.marks_for_labs.append(mark)
            return  1
        else:
            return 0

    def get_tries_ind(self, try_pass, mark):
        if  int(mark) < int(self.max_marks_i) and self.max_marks_i != None:
            passed_try = random.randint(int(0), int(try_pass))
            if passed_try >= 1:
                self.mark_for_ind = random.randint(int(mark), int(self.max_marks_i))
            else:
                self.mark_for_ind = mark
            return 1
        else:
            return 0


    def get_res(self):
        num = int(self.mark_for_ind)
        for mark in self.marks_for_labs:
            num += int(mark)
        if num >= self.marks_part:
            log_val = True
        else:
            log_val = False
        return (num, log_val)

def input_int_digit(string):
    """
    Return int number

    Parameters
    ----------
    string : what write in input.

    Returns
    -------
    number : int number.

    """
    while True:
        number = input(string)
        if(number.isdigit() and int(number) >= 0):
            return number
if __name__ == '__main__':
    name = input("Введіть ім'я студента: ")
    
    mark_lab = input_int_digit("Введіть максимальну оцінку за здачу лабораторної роботи: ")
        
    
    mark_ind = input_int_digit("Введіть максимальну оцінку за здачу індивідуального завдання: ")
    labs = input_int_digit("Введіть кількість лабораторних робіт: ")
    res_mark = input_int_digit("Введіть кількість балів, що потрібно набрати студенту: ")
    dict = {'max_marks_ind':int(mark_ind),'max_marks_lab':int(mark_lab),'count_labs':int(labs), 'marks_for_passing':int(res_mark)} 
    
    Stud = Student(name, **dict)
    try_pass_l = input_int_digit("Введіть кількість спроб здати лабораторну роботу: ")
    min_mark_l = input_int_digit("Введіть оцінку за здачу лабораторної роботи з останньої спроби: ")
    try_pass_i = input_int_digit("Введіть кількість спроб здати індивідуальну роботу: ")
    min_mark_i = input_int_digit("Введіть оцінку за здачу індивідуальної роботи з останньої спроби: ")
    
    if Stud.get_tries_lab(try_pass_l, min_mark_l) and Stud.get_tries_ind(try_pass_i, min_mark_i):
        print("Успішність студента:" + str(Stud.get_res()))
    else:
        print("Помилка обробки данних студента :( " + str(Stud.get_tries_lab(try_pass_l, min_mark_l)))
