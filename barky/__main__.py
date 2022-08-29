import click
import barky
import sys


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

    title = title if title else "[+] Barky"
    message = message if message else "PING"

    if remote:
        barky.notify_remotelly(title, message)
    if local:
        barky.notify_locally(title, message)

    if not remote and not local:
        barky.notify_remotelly(title, message)
        barky.notify_locally(title, message)

main()
