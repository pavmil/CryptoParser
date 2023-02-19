import telebot


def send_notify(message):
    chat_id = "" # your api hash
    api_hash =  0# your chat id
    
    bot = telebot.TeleBot(api_hash) 
    bot.send_message(chat_id, message)
