import pyautogui as clicker
import pandas as pd
import schedule
import time


def openWhatsappAndSend(phone, message):
    url = "https://web.whatsapp.com/send?phone=" + \
        phone+"&text=" + message + "&app_absent=1"
    start = clicker.locateCenterOnScreen('opera.png')
    clicker.moveTo(start)
    clicker.click()
    clicker.hotkey('ctrl', 't')
    search = clicker.locateCenterOnScreen('search.png')
    clicker.moveTo(search)
    clicker.click()
    clicker.typewrite(url)
    clicker.press('enter')
    time.sleep(10)
    clicker.press('enter')
    time.sleep(2)
    clicker.hotkey('ctrl', 'w')


def sendAll(users):
    for user in range(0, len(users)):
        phone = users["Phone"][user]
        message = users["Message"][user]
        openWhatsappAndSend(phone, message)


if __name__ == "__main__":

    users = pd.read_csv("users.csv")
    usersLength = len(users)
    if(usersLength > 1):
        schedule.every().day.at("02:17").do(sendAll(users))
        schedule.run_pending()
        time.sleep(1)

    else:
        print("Mesaj gönderilecek kullanıcı sayısı 0")
