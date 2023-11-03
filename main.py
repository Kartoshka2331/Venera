import telebot

from anti_spam import *
from translator import *
from logger import *

from methods.number import *
from methods.ip import *
from methods.nickname import *

bot = telebot.TeleBot("6507203007:AAGp9HtrputlDwmVrodT07kwpaMEyAugGTg")

@bot.message_handler(content_types=["text"])
def get_message(message):
    if anti_spam(str(message.chat.id)): return

    if message.text == "/start" or message.text == "/help":
        bot.send_photo(message.chat.id, "https://i.imgur.com/aLfTbfo.png", get_translation("Welcome_message", message.from_user.language_code).replace("{var1}", "/number").replace("{var2}", "/email").replace("{var3}", "/ip").replace("{var4}", "/nickname"))

    else:
        if message.text.startswith("/number "):
            handling = bot.send_message(message.chat.id, "💬")
            bot.edit_message_text(chat_id = message.chat.id, message_id = handling.message_id, text = check_number(message.text.replace("/number ", ""), message.from_user.language_code))
        elif message.text.startswith("/email "):
            handling = bot.send_message(message.chat.id, "💬")
            bot.edit_message_text(chat_id = message.chat.id, message_id = handling.message_id, text = check_email(message.text.replace("/email ", ""), message.from_user.language_code))
        elif message.text.startswith("/ip "):
            handling = bot.send_message(message.chat.id, "💬")
            bot.edit_message_text(chat_id = message.chat.id, message_id = handling.message_id, text = check_ip(message.text.replace("/ip ", ""), message.from_user.language_code))
        elif message.text.startswith("/nickname "):
            handling = bot.send_message(message.chat.id, "💬")
            bot.edit_message_text(chat_id = message.chat.id, message_id = handling.message_id, text = check_nickname(message.text.replace("/nickname ", ""), message.from_user.language_code))
        else:
            handling = bot.send_message(message.chat.id, "💬")
            bot.edit_message_text(chat_id = message.chat.id, message_id = handling.message_id, text = get_translation("Unknown_command", message.from_user.language_code).replace("{var1}", "/help"))

@bot.message_handler(content_types=["photo"])
def get_message(message):
    if anti_spam(str(message.chat.id)): return

    handling = bot.send_message(message.chat.id, "💬")
    bot.send_message(message.chat.id, check_photo(bot.download_file(bot.get_file(message.document.file_id).file_path), message.from_user.language_code))
    bot.delete_message(message.chat.id, handling.message_id)

if __name__ == "__main__":
    log("Starting", "message")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
