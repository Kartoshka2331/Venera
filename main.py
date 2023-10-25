import telebot

from anti_spam import *
from translator import *
from logger import *

from methods.number import *

bot = telebot.TeleBot("6507203007:AAGp9HtrputlDwmVrodT07kwpaMEyAugGTg")

@bot.message_handler(content_types=["text"])
def get_message(message):
    if anti_spam(str(message.chat.id)): return

    if message.text == "/start" or message.text == "/help":
        bot.send_photo(message.chat.id, "https://i.imgur.com/aLfTbfo.png", get_translation("Welcome_message", message.from_user.language_code).replace("{var1}", "/number").replace("{var2}", "/email").replace("{var3}", "/ip").replace("{var4}", "/nickname"))

    else:
        if message.text.startswith("/number "):
            bot.send_message(message.chat.id, check_number(message.text.replace("/number ", "")))
        elif message.text.startswith("/email "):
            bot.send_message(message.chat.id, check_email(message.text.replace("/email ", "")))
        elif message.text.startswith("/ip "):
            bot.send_message(message.chat.id, check_ip(message.text.replace("/ip ", "")))
        elif message.text.startswith("/nickname "):
            bot.send_message(message.chat.id, check_nickname(message.text.replace("/nickname ", "")))
        else:
            bot.send_message(message.chat.id, get_translation("Unknown_command", message.from_user.language_code).replace("{var1}", "/help"))

@bot.message_handler(content_types=["photo"])
def get_message(message):
    if anti_spam(str(message.chat.id)): return

    bot.send_message(message.chat.id, check_photo(bot.download_file(bot.get_file(message.document.file_id).file_path)))

if __name__ == "__main__":
    log("Starting", "message")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
