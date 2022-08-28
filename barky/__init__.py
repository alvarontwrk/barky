from notifypy import Notify
import telegram
import os


def notify_locally(title: str, body: str):
    notification = Notify()
    notification.title = title
    notification.message = body
    notification.icon = "barky/icon.png"

    notification.send()


def notify_remotelly(title: str, body: str):
    chat_id = os.environ["BARKY_TG_CHAT"]
    token = os.environ["BARKY_TG_TOKEN"]

    text = "{}\n\n{}".format(title, body)

    bot = telegram.Bot(token)
    bot.send_message(chat_id, text)


def main():
    notify_locally("Title", "This is the body")
    notify_remotelly("Title", "This is the body")
