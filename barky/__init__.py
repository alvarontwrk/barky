import notifypy
import telegram
import os


def notify_locally(title: str, body: str):
    notification = notifypy.Notify()
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
