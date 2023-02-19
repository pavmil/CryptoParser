import telebot


def send_notify(message):
    bot = telebot.TeleBot("6263162578:AAGuGsiKF7_WoOiZ4dptCqry-ZkishL6w1o") # your api hash
    bot.send_message(423979863, message) # your chat id