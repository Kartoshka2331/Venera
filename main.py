from datetime import datetime
from deep_translator import GoogleTranslator
import telebot
import time

bot = telebot.TeleBot("6507203007:AAHqYjiI05OydfD38llWSlV5Ywu9IBl7dJw")
last_message_times = {}

def log(message, log_type):
    timestamp = datetime.now().strftime("%m.%d.%Y %H:%M:%S")
    with open("logs.txt", "a") as file:
        file.write(f"{timestamp} : {log_type} : {message}\n")

def get_translation(argument, language):
    with open("phrases.txt", "r") as file:
        with open("phrases.txt", "r") as file_len:
            for x in range(len(file_len.readlines())):
                argument_temp = file.readline().split(" - ")
                if argument_temp.pop(0) == argument:
                    return GoogleTranslator(source="en", target=language).translate(argument_temp.pop(0))

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
        bot.send_photo(message.chat.id, "https://i.imgur.com/aLfTbfo.png", get_translation("instruction", message.from_user.language_code))
    else:
        print("!")
        print("!")
        print("!")

if __name__ == "__main__":
    log("Starting", "message")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
