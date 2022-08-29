import notifypy
import telegram
import importlib.metadata

# Get version from pyproject.toml
__version__ = importlib.metadata.version("barky")


def notify_locally(title: str, body: str):
    notification = notifypy.Notify()
    notification.title = title
    notification.message = body
    try:
        notification.icon = __path__[0] + "/icon.png"
    # Catch exception in case icon is finally not found
    except notifypy.exceptions.InvalidIconPath:
        notification.icon = ""

    notification.send()


def notify_remotelly(title: str, body: str, chat_id: str, token: str):
    text = "{}\n\n{}".format(title, body)

    bot = telegram.Bot(token)
    bot.send_message(chat_id, text)
