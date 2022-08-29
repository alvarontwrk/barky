import notifypy
import telegram
import os
import pkgutil

# This is needed to find icon.png in the package directory
pkgutil.extend_path(__path__, __name__)


def notify_locally(title: str, body: str):
    notification = notifypy.Notify()
    notification.title = title
    notification.message = body
    notification.icon = "icon.png"

    notification.send()


def notify_remotelly(title: str, body: str):
    chat_id = os.environ["BARKY_TG_CHAT"]
    token = os.environ["BARKY_TG_TOKEN"]

    text = "{}\n\n{}".format(title, body)

    bot = telegram.Bot(token)
    bot.send_message(chat_id, text)
