import csv
import os
from modulesPROKOPENKO import quickSort
def read_table_file(name_file="kb_20_marks_table.csv", char_split=";", encoding_file="utf-8"):
    try:
        with open(name_file, mode="r", encoding=encoding_file) as file:
            col = []
            col_cout = 0
            for line in file:
                line = str(line).replace('\n', '')
                if(col_cout == 0):
                    col.insert(col_cout,line.split(char_split))
                else:
                    col.insert(col_cout,line.split(char_split,maxsplit = len(col[0])))
                col_cout += 1
            
            return col
    except FileNotFoundError:
        print("Помилка! файл " + name_file + " не існує!")


def create_csv_file(name_table="kb_20_marks_table", char_split_console=";", char_split=";", encoding_file="utf-8", format_table=".csv"):
    try:
        with open(name_table + format_table, "a+") as file:
            f = csv.writer(file, delimiter=char_split, lineterminator="\r")
            print("Розділяйте кожну вашу заплановану клітинку у таблиці символом:" +
                  char_split_console + "\n")
            print("А для завершення процесу створеня введіть таке слово: q!\n")

            cout_str = 0
            string = None
            while True:
                if string == None:
                    print("Введіть Заголовки Вашої таблиці:")
                else:
                    print("Введіть " + str(cout_str) +
                          " \"строку\" Вашої таблиці: ")
                string = input().split(char_split_console)
                if(len(string) == 1 and string[0] == "q!"):
                    print("Таблиця " + name_table +
                          format_table + " успішно створена!")
                    break
                cout_str += 1

                f.writerow(string)
    except FileNotFoundError:
        print("Помилка! файл " + name_table + " не існує!")


def seach_in_table(what_seach,name_file="kb_20_marks_table.csv", char_split_console=";", char_split=";", encoding_file="utf-8"):
    table_in_list = read_table_file(name_file, char_split, encoding_file)
    for col in range(len(table_in_list)):
        for row in range(len(table_in_list[0])):
            if(table_in_list[col][row] == what_seach):
                return [col,row]
    return None

def seach_file(name_file="kb_20_marks_table.csv", path = './'):
    for r, d, f in os.walk(path):
        for file in f:
            if str(file) == str(name_file):
                return os.path.abspath(os.path.join(r,file))
    return None
             
def sort_student(name_file="kb_20_marks_table.csv", char_split=";", encoding_file="utf-8", path_for_seach = '.|'):
    
    if(seach_file(name_file) != None): 
        
        marks = []
        table_in_list = read_table_file(name_file,char_split,encoding_file)
        table_in_list[0].append("Cередній бал студента")
        for col in range(1,len(table_in_list)):
            student_mark = 0
            for row in range(3,len(table_in_list[0])-1):
             
                student_mark  += int(table_in_list[col][row])
                
            marks.append(student_mark/(len(table_in_list[0])-4))
            table_in_list[col].append(student_mark/(len(table_in_list[0])-4))
        sort_marks = quickSort(marks)
        
        position = 0
        new_table = []
        new_table.append(table_in_list[0].copy())
        for sort_mark in sort_marks:
            position +=1
            
            for i in range(len(marks)):
                if marks[i] == sort_mark:
                    table_in_list[i+1][0] = position
                    new_table.append(table_in_list[i+1].copy())
                   
                    
                    marks[i] = -1
                    
                    break;
   
       
        with open("sort_"+ name_file, "w",encoding=encoding_file) as file:
            f = csv.writer(file, delimiter=char_split, lineterminator="\r")
               
            for col in range(len(new_table)):
               
                f.writerow(new_table[col])
    
        
                    
            
def write_in_table_end(what_write, name_file="sort_kb_20_marks_table.csv", char_split=";", encoding_file="utf-8"):
     if(seach_file(name_file)):
         table_in_list = read_table_file(name_file,char_split,encoding_file)
         what_write = str(what_write).replace('\n', '')
         length = len(table_in_list)
         table_in_list.insert(length,what_write.split(char_split,maxsplit = len(table_in_list[0])))
         with open(name_file, "w") as file:
            f = csv.writer(file, delimiter=char_split, lineterminator="\r")
            for col in range(len(table_in_list)):
                f.writerow(table_in_list[col])
         
    
                          
            
    

if __name__ == "__main__":
    
    print(seach_in_table("lol"))
    