import click
import barky


@click.command()
@click.argument("body")
@click.option("-t", "--title", type=str)
@click.option("-r", "--remote", is_flag=True)
@click.option("-l", "--local", is_flag=True)
def main(body, title, remote, local):
    title = title if title else "[+] Barky"
    if remote:
        barky.notify_remotelly(title, body)
    if local:
        barky.notify_locally(title, body)

    if not remote and not local:
        barky.notify_remotelly(title, body)
        barky.notify_locally(title, body)
