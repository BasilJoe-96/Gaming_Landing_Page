import time
import telebot #da questo errore perché manca l'API di telegram?


greeting = """
    Welcome to Chat bot!
You can write a text or send an image to receive an answer to your problem encountered in the game.
"""

help_ = """
To find a quick answer write @Gamebot and keywords of your problem.
Inside a chat you can use /faq command to get a brief info.
Example:
/faq dark screen
If you want explore the faqs, you can type /allfaq.
If you want send the image
"""

Token = ''
bot = telebot.TeleBot(Token)
darkscreen = darkscreen() #qui dovrei creare un altro file .py per definire la funzione?

#/start in all message
@bot.message_handler(commands=['start'])  # greeting
def send_welcome(message):
    bot.reply_to(message.chat.id, greeting)

#command list
@bot.message_handler(commands=['help'])  # command list
def send_welcome(message):
    bot.reply_to(message.chat.id, help_)

#FAQ commands
@bot.message_handler(commands=['faq'])  # /allfaq
def faq(message):
    text = "Your result: {}".format(text(darkscreen['Possible solutions:']))
    bot.send_message(message.chat.id, text)

@bot.photo_handler(command=['image'])
def image(message):
    text = "I Found These: {}".format()
    bot.send_message(message.chat.id,text) 
    #qui dovrei creare un altro file affinché il bot riesca a decifrare l'immagine
    #e dare una risposta. Un po' too much al momento

