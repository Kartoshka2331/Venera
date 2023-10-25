from deep_translator import GoogleTranslator

phrases = {}

with open("phrases.txt", "r") as file:
    for string in file.readlines():
        splited_string = string.split(" --- ")
        if len(splited_string) != 2:
            break
        phrases[splited_string[0]] = splited_string[1].replace("\\n", "\n")

def get_translation(argument, language):
    return GoogleTranslator(source="en", target=language).translate(phrases[argument])