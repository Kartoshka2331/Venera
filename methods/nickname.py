from selenium import webdriver
from selenium.webdriver.common.by import By

def check_nickname(nickname, user_language_code):
    driver = webdriver.Firefox()

    to_return = []

    # YouTube
    try:
        driver.get(f"https://www.youtube.com/@{nickname}")
        user_agreement = driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.iMLaPd")
        user_agreement.click()
        driver.find_element(By.CSS_SELECTOR, ".style-scope.ytd-channel-name")
        to_return.append(f"✅YouTube - https://www.youtube.com/@{nickname}")
    except:
        to_return.append("❌YouTube")

    # TikTok
    try:
        driver.get(f"https://www.tiktok.com/@{nickname}")
        driver.find_element(By.CSS_SELECTOR, ".tiktok-1xo9k5n-H1ShareTitle.e1457k4r8")
        to_return.append(f"✅TikTok - https://www.tiktok.com/@{nickname}")
    except:
        to_return.append("❌TikTok")

    # Instagram
    try:
        driver.implicitly_wait(1)
        driver.get(f"https://www.instagram.com/{nickname}")
        driver.find_element(By.CSS_SELECTOR, ".x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.x1ms8i2q.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")
        to_return.append(f"✅Instagram - https://www.instagram.com/{nickname}")
    except:
        to_return.append("❌Instagram")

    # Telegram
    try:
        driver.get(f"https://t.me/{nickname}")
        driver.find_element(By.CSS_SELECTOR, ".tgme_page_extra")
        to_return.append(f"✅Telegram - https://t.me/{nickname}")
    except:
        to_return.append("❌Telegram")

    # VK
    try:
        driver.get(f"https://vk.com/{nickname}")
        driver.find_element(By.CSS_SELECTOR, ".vkuiTypography.vkuiTypography--normalize.vkuiTypography--weight-1.OwnerPageName.vkuiTitle--level-2")
        to_return.append(f"✅VK - https://vk.com/{nickname}")
    except:
        to_return.append("❌VK")

    # Twitter
    try:
        driver.get(f"https://twitter.com/{nickname}")
        driver.find_element(By.CSS_SELECTOR, ".css-901oao.css-1hf3ou5.r-1bwzh9t.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-qvutc0")
        to_return.append(f"✅Twitter - https://twitter.com/{nickname}")
    except:
        to_return.append("❌Twitter")

    # Twitch
    try:
        driver.implicitly_wait(1)
        driver.get(f"https://www.twitch.tv/{nickname}")
        driver.find_element(By.CSS_SELECTOR, ".CoreText-sc-1txzju1-0.ScTitleText-sc-d9mj2s-0.AAWwv.ezNtJL.InjectLayout-sc-1i43xsx-0.dhkijX.tw-title")
        to_return.append(f"✅Twitch - https://www.twitch.tv/{nickname}")
    except:
        to_return.append("❌Twitch")


    final_result = ""
    for x in to_return:
        final_result += x + "\n"

    driver.close()

    return final_result