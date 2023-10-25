from datetime import datetime

def log(message, log_type):
    timestamp = datetime.now().strftime("%m.%d.%Y %H:%M:%S")
    with open("logs.txt", "a") as file:
        file.write(f"{timestamp} : {log_type} : {message}\n")