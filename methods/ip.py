import re
import geocoder

from translator import *
from logger import *

def check_ip(IP, user_language_code):
    ip_regex = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    if re.match(ip_regex, IP):
        octets = IP.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            try:
                geocoder_IP = geocoder.ip(IP)
                coordinates = (geocoder_IP.latlng[0], geocoder_IP.latlng[1])
                return get_translation("ip_format", user_language_code).replace("{var1}", str(IP)).replace("{var2}", str(geocoder_IP.country)).replace("{var3}", str(geocoder_IP.state)).replace("{var4}", str(geocoder_IP.org)).replace("{var5}", str(geocoder_IP.city)).replace("{var6}", str(coordinates)).replace("{var7}", str(geocoder.google(coordinates, method='reverse').address)).replace("{var8}", str(f"https://maps.google.com/maps?q={coordinates[0]},{coordinates[1]}"))
            except Exception as error:
                log("Checking of ip address " + IP + " was failed ''" + str(error) + "''", "message")
                return get_translation("Invalid_ip", user_language_code).replace("{var1}", IP)
    return get_translation("Invalid_ip", user_language_code).replace("{var1}", IP)