import telebot
import random
bot = telebot.TeleBot('1833568218:AAFvsaKqwOaw3NzhJUXsLmdY70wJpwzZglw')


def list_in_file(file_name,path_of_file = "./",encoding_file = "utf-8",split_symbol = '\n'):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           array = []
           f = file.read()
               
           array = f.split(split_symbol)
           return array
           
cats_image = list_in_file("cats.txt")
citats = list_in_file("citat.txt",split_symbol=";;")
stikers = list_in_file("stikers.txt")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
@bot.message_handler(commands=['help_me_pls','help'])
def send_help(message):
    bot.reply_to(message, 'Я можу виконувати такі команди:\n/start\n/help_me_pls\n/random_stiker\n/random_image\n/random')
@bot.message_handler(commands=['text'])
def text(message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.from_user.id, 'Привіт! Що будете робити?')
    else:
        bot.reply_to(message, f'{message.from_user.first_name}, Я не розумію Вас...\n/help_me_pls')

@bot.message_handler(commands=['random'])
def randoms(message):
    img = random.choice(cats_image)
    text = random.choice(citats)
    bot.reply_to(message, f' {text} <a href="{img}">&#8203;</a>', parse_mode="HTML")
@bot.message_handler(commands=['random_stiker'])
def random_stiker(message):
    bot.send_sticker(message.chat.id, random.choice(stikers))
@bot.message_handler(commands=['random_image'])
def random_image(message):
    img = random.choice(cats_image)
    bot.send_photo(message.chat.id,img) 
bot.polling(none_stop=True)