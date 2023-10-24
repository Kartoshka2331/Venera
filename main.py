from datetime import datetime
from deep_translator import GoogleTranslator
import telebot
import time

from methods.TEST import *

bot = telebot.TeleBot("6507203007:AAHqYjiI05OydfD38llWSlV5Ywu9IBl7dJw")
last_message_times = {}
phrases = {}

with open("phrases.txt", "r") as file:
    for string in file.readlines():
        splited_string = string.split(" --- ")
        if len(splited_string) != 2:
            break
        phrases[splited_string[0]] = splited_string[1].replace("\\n", "\n")

def log(message, log_type):
    timestamp = datetime.now().strftime("%m.%d.%Y %H:%M:%S")
    with open("logs.txt", "a") as file:
        file.write(f"{timestamp} : {log_type} : {message}\n")

def get_translation(argument, language):
    return GoogleTranslator(source="en", target=language).translate(phrases[argument])

@bot.message_handler(content_types=["text"])
def get_message(message):
    chat_id = str(message.chat.id)
    current_time = time.time()
    if chat_id not in last_message_times:
        last_message_times[chat_id] = current_time
    elif current_time - last_message_times[chat_id] > 1:
        last_message_times[chat_id] = current_time
    else:
        last_message_times[chat_id] = current_time
        return

    if message.text == "/start":
        bot.send_photo(message.chat.id, "https://i.imgur.com/aLfTbfo.png", get_translation("Welcome_message", message.from_user.language_code).replace("{var1}", "/number").replace("{var2}", "/email").replace("{var3}", "/ip").replace("{var4}", "/nickname").replace("{var5}", "/photo"))
    else:
        if message.text.startswith("/ip "):
            message_text = message.text.replace("/ip ", "")
            bot.send_message(message.chat.id, TEST(message_text))

if __name__ == "__main__":
    log("Starting", "message")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
