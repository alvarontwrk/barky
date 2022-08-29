import notifypy
import telegram
import importlib.metadata

# Get version from pyproject.toml
__version__ = importlib.metadata.version("barky")

# Export the exception
BinaryNotFound = notifypy.exceptions.BinaryNotFound


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
    text = "{}\n\n{}".format(title.strip(), body.strip())
    bot = telegram.Bot(token)
    print(len(text))
    if len(text) > telegram.constants.MAX_MESSAGE_LENGTH:
        for i in range(0, len(text), telegram.constants.MAX_MESSAGE_LENGTH):
            print(text[i:i+telegram.constants.MAX_MESSAGE_LENGTH])
            bot.send_message(chat_id,
                             text[i:i+telegram.constants.MAX_MESSAGE_LENGTH])
    else:
        bot.send_message(chat_id, text)
