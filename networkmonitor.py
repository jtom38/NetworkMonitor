
import click

from networkmonitor.tui import uiMain

#@click.command()
#def cfg():
#    click.echo(f"Do the thing {cfg}!")

@click.command()
@click.option('--config', default='config.json', help='json configuration file to load')
def init(config):
    """
    Init is the applications start point.  From here we will call in what we need.

    """
    main = uiMain(config)
    main.Start()

if __name__ == "__main__":
    init()