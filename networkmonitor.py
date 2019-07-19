
import click

from networkmonitor.tui import uiMain

#@click.command()
#def cfg():
#    click.echo(f"Do the thing {cfg}!")

@click.command()
@click.option('--config', default='config.json', help='json configuration file to load')
@click.option('--newconfig', default=False, help='Generates a new configuration file')
def init(config):
    """
        NetorkMonitor is a curses tool to monitor network nodes.
        Currently supports ping(icmp), Http: Get and Post.

        To get started:

        networkmonitor --config "demo.json" --newconfig

    """
    main = uiMain(config)
    main.Start()

if __name__ == "__main__":
    init()