from tabulate import tabulate


header = input("Header table: \n").split("  ")

table = []
while True:
    string = input().split(";")
    if( len(string) == 1 and string[0] == "quit"):
        break
    table.append(string)

    
file_name = input("введите имя вашего файла")     
with open(file_name +".txt", "w") as f:
    print (tabulate(table, header, tablefmt="grid",stralign='center'),file = f)
    
   
    
    

