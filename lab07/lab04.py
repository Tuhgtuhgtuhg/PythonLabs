from lab03 import seach_file
import random

def random_sentence(list1,list2,list3):
    return random.choice(list1) + " " + random.choice(list2) + " " + random.choice(list3)
    

def how_word_in_file(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           words = 0
           for string in file:
               for letter in string:
                   if( letter.isalpha() == False and letter != ' ' ):
                       string = string.replace(letter,'')
               words += len(list(filter(None, str(string).split(' '))))
           return words
   return 0

def symbols_in_text(file_name,path_of_file = "./",encoding_file = "utf-8"):
    if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           symbols = 0
           for string in file:
               symbols += len(str(string))
               
                   
           return symbols
    return 0

def symbols_in_text_no_gap(file_name,path_of_file = "./",encoding_file = "utf-8"):
    if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           symbols = 0
           for string in file:
               symbols += len(str(string).replace(' ',''))
               
                   
           return symbols
    return 0

def how_word_in_file_no_replay(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           words = 0
           no_replay_words = []
           for string in file:
               
               string = str(str(string).upper())
               
               for letter in string:
                   if( letter.isalpha() == False and letter != ' ' ):
                       string = string.replace(letter,'')
                       
               string = list(filter(None, str(string).split(' ')))
               words += len(string)
               for word in string:
                       
                   unical = True
                   if(len(no_replay_words) == 0):
                           no_replay_words.append(word)
                   else:
                           for reply in no_replay_words:
                               if word == reply or word == '':
                                   unical = False
                                   words -= 1
                                   break
                           if(unical):
                               no_replay_words.append(word)                   
           return words
   return 0

def how_word_in_file_unical(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           words = 0
           no_replay_words = []
           frequency_words = []
           for string in file:
               string = str(str(string).upper())
               
               for letter in string:
                   if( letter.isalpha() == False and letter != ' ' ):
                       string = string.replace(letter,'')
                       
               string = list(filter(None, str(string).split(' ')))
               words += len(string)
               for word in string:
                       
                   unical = True
                   if(len(no_replay_words) == 0):
                           no_replay_words.append(word)
                           frequency_words.append(1)
                   else:
                           for reply in no_replay_words:
                               if word == reply or word == '':
                                   frequency_words[no_replay_words.index(reply)] += 1
                                   unical = False
                                   words -= 1
                                   break
                           if(unical):
                               no_replay_words.append(word)
                               frequency_words.append(1)
           words = 0
           for cout in frequency_words:
               if cout == 1:
                   words += 1
                               
           return words
   return 0

def how_sentences_in_file(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           
           sentense = 0
           for string in file:
               string = str(str(string).upper())
               sentense += len(list(find_all(str(string),'!')))
               sentense += len(list(find_all(str(string),'.')))
               sentense += len(list(find_all(str(string),'?')))
               sentense += len(list(find_all(str(string),'...')))-len(list(find_all(str(string),'...')))*3
           return sentense
   return 0
def how_sentences_in_file_question(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           
           sentense = 0
           for string in file:
               string = str(str(string).upper())
               sentense += len(list(find_all(str(string),'?')))
           return sentense
   return 0

def how_sentences_in_file_exclamatory(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           
           sentense = 0
           for string in file:
               string = str(str(string).upper())
               sentense += len(list(find_all(str(string),'!')))
           return sentense
   return 0


def how_sentences_in_file_normal(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           
           sentense = 0
           for string in file:
               string = str(str(string).upper())
               sentense += len(list(find_all(str(string),'.'))) - len(list(find_all(str(string),'...')))*3
           return sentense
   return 0

def how_sentences_in_file_three_dots(file_name,path_of_file = "./",encoding_file = "utf-8"):
   if (seach_file(file_name,path_of_file) != None):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           
           sentense = 0
           for string in file:
               string = str(str(string).upper())
               sentense += len(list(find_all(str(string),'...')))
           return sentense
   return 0
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)    
if __name__ == '__main__':
    list1 = ["Наруто","Оксана","Влад","Андрій","Котик","Артем","Тетяна","Дарина","Єлизавета","Егор","Жабка"]
    list2 = ["лопає","сідає","спить","наївся","страждає","відпочиває","лежить","стоїть","снідає","живе","нюхає"]
    list3 = ["у ЦНТУ","вдома","на заводі","на сесії","на пуфику","на кладовищі","на стілець","на вулиці","у літаку"]
    print(random_sentence(list1, list2, list3))
    print(how_word_in_file_unical("SPOILER_.txt"))
    
          