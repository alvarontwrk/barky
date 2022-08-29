import click
import barky
import sys
import os


@click.command()
@click.option("-t", "--title", type=str)
@click.option("-m", "--message", type=str)
@click.option("-r", "--remote", is_flag=True)
@click.option("-l", "--local", is_flag=True)
@click.version_option()
def main(message, title, remote, local):
    """
    Priority for message:
        1. Option -m
        2. STDIN
        3. "PING"
    """
    if not sys.stdin.isatty() and not message:
        message = "".join(sys.stdin.readlines())
        print(message)

    title = title if title else "Barky"
    message = message if message else "PING"
    chat_id = os.environ.get("BARKY_TG_CHAT", "")
    token = os.environ.get("BARKY_TG_TOKEN", "")

    if not chat_id or not token:
        print("Need to specify the following environment variables:")
        print("\t- BARKY_TG_CHAT: Telegram chat ID")
        print("\t- BARKY_TG_TOKEN: Telegram bot token")
        sys.exit(1)

    if remote:
        barky.notify_remotelly(title, message, chat_id, token)
    if local:
        try:
            barky.notify_locally(title, message)
        except barky.BinaryNotFound as e:
            print(("Local notification not supported. The following "
                   "binary is needed: {}".format(e.args[0])))

    if not remote and not local:
        barky.notify_remotelly(title, message, chat_id, token)
        try:
            barky.notify_locally(title, message)
        # If the binary is not found here, just omit it
        except barky.BinaryNotFound:
            pass


main()
