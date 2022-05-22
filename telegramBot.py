import time
import telebot
import telegram_send

file = open("information.txt")
token_id = file.readline()
file.close()
token =token_id

def send_mes_to_bot(message1):
    telegram_send.send(messages=[message1])
# def telegram_bot(token):
    #bot = telebot.TeleBot(token)
    # @bot.message_handler(commands=["start"])
    # def start_message(message):
    #     bot.send_message(message.chat.id, "Приветствую тебя, будщий бизнесмен, давай начнем!")
    #
    # @bot.message_handler(content_types=["text"])
    # def send_text(message):
#     #     bot.send_message(message.chat.id, "привет")

    # def send_text(message):
    #     bot.send_message(message.chat.id, "привет")
