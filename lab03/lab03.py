import csv


def lol(name_file = "kb_20_marks_table.csv",char_split =";",encoding_file = "utf-8"):
    try:
        with open (name_file,mode="r",encoding = encoding_file) as file:
            col = []
            col_cout = 0
            for line in file:
                col.append([])
                col[col_cout].append(line.split(char_split))
                col_cout += 1
            return col;
    except FileNotFoundError:
        print("Помилка! файл " + name_file +" не існує!")

def create_table_file(name_table = "kb_20_marks_table",char_split_console =";", char_split = ";", encoding_file = "utf-8",format_table = ".csv"):
    try:
        with open(name_table + format_table, "a+") as file:
            f = csv.writer(file, delimiter = char_split, lineterminator="\r")
            print("Розділяйте кожну вашу заплановану клітинку у таблиці символом:" + char_split_console + "\n")
            print("А для завершення процесу створеня введіть таке слово: q!\n")
            
            cout_str = 0
            string = None
            while True:
                if string == None:
                    print("Введіть Заголовки Вашої таблиці:")
                else:
                    print("Введіть " + str(cout_str) + " \"строку\" Вашої таблиці: ")
                string = input().split(char_split_console)
                if( len(string) == 1 and string[0] == "q!"):
                    print("Таблиця "+ name_table + format_table + " успішно створена!")
                    break
                cout_str += 1
                
                
                    
                f.writerow(string)
    except FileNotFoundError:
        print("Помилка! файл " + name_table +" не існує!")
        
        
if __name__ == "__main__":
    file_name = input("введите имя вашего файла\n")
    #create_table_file(file_name)
    print(lol("lisa.csv"))
    
    
        
    
        
        
        

