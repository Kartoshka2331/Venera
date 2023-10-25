import time

last_message_times = {}

def anti_spam(chat_id):
    current_time = time.time()
    if chat_id not in last_message_times:
        last_message_times[chat_id] = current_time
    elif current_time - last_message_times[chat_id] > 1:
        last_message_times[chat_id] = current_time
    else:
        last_message_times[chat_id] = current_time
        return True
    return False
