import notifypy
import telegram
import os
import click


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


@click.command()
@click.argument("body")
@click.option("-t", "--title", type=str)
@click.option("-r", "--remote", is_flag=True)
@click.option("-l", "--local", is_flag=True)
def main(body, title, remote, local):
    title = title if title else "[+] Barky"
    if remote:
        notify_remotelly(title, body)
    if local:
        notify_locally(title, body)

    if not remote and not local:
        notify_remotelly(title, body)
        notify_locally(title, body)
