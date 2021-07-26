from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import (
    GetHistoryRequest,
    GetBotCallbackAnswerRequest,
)
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os

try:
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
except:
    print(
        "\033[1;30m# \033[1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4"
    )
    sys.exit()



c = requests.Session()



if not os.path.exists("session"):
    os.makedirs("session")

if len(sys.argv) < 2:
    print("\n\n\n\033[1;32mUsage : python main.py +62")
    sys.exit(1)


def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "\033[1;0m#\033[1;0m{:2d} \033[1;0mseconds remaining".format(remaining)
        )
        sys.stdout.flush()
        sleep(1)


ua = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
}


api_id = 974754
api_hash = "6295657bbae725bfe8dfcca5d9e323e6"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input("\n\n\n\033[1;0mEnter Your Code : "))
    except SessionPasswordNeededError:
        passw = input("\033[1;0mYour 2fa Password : ")
        me = client.start(phone_number, passw)
myself = client.get_me()
os.system("clear")
print(
    "\033[1;32mYour Name   \033[1;33m:\033[1;0m",myself.first_name,
    "\n\033[1;32mYour Number \033[1;33m:\033[1;0m",sys.argv[1],
    "\n\033[1;32mTelebot     \033[1;33m: \033[1;32m-WD (Clickbot)"
)
print("\033[1;32m================================================")

#password()
print("\n\033[1;37mRun Bot......!\n")

try:
    channel_entity = client.get_entity("@Litecoin_click_bot")
    channel_username = "@Litecoin_click_bot"
    for i in range(5000000):
        
            sys.stdout.write('\r')
            sys.stdout.write('                                                              ')
            sys.stdout.write('\r')
            sys.stdout.write('\x1b[1;32mStatus Withdraw : \x1b[1;32mGathering info ... !')
            sys.stdout.flush()
            client.send_message(entity=channel_entity, message='/Balance')
            sleep(1)
            posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            message = posts.messages[0].message
            bal = re.findall('([\\d.]*\\d+)', message)[0]
            client.send_message(entity=channel_entity, message='/Withdraw')
            sleep(1)
            posts_ = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            if posts_.messages[0].message.find('Your balance is too small to') != -1:
                sys.stdout.write(f"\r\x1b[1;32mStatus Withdraw : \x1b[1;32mAvailable balance {bal} \n\n")
                sleep(1)
            else:
                client.send_message(entity=channel_entity, message='/ENTER WALLET')
                sleep(1)
                client.send_message(entity=channel_entity, message=bal)
                sleep(1)
                client.send_message(entity=channel_entity, message='/Confirm')
                sys.stdout.write(f"\r\x1b[1;32mStatus Withdraw : \x1b[1;32mSuccess withdraw {bal} \n\n")
                sleep(1)
            sys.exit()   
        
finally:
    client.disconnect()