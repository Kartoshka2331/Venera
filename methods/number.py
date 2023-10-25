from translator import *
def check_number(number, user_language_code):
    return get_translation("Invalid_number", user_language_code).replace("{var1}", number)