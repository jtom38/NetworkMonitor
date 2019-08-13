
import click

from networkmonitor.src.configuration import IConfig, JsonConfig, YamlConfig, ContextConfig 
from networkmonitor.src import CLI

from networkmonitor.tui import uiMain

#@click.command()
#def cfg():
#    click.echo(f"Do the thing {cfg}!")

@click.command()
@click.option('--config', default='example.yaml', help='json or yaml configuration file to load')
@click.option('--newconfig', default=False, help='Generates a new configuration file')
def init(config:str, newconfig:bool):
    """
        NetworkMonitor is a curses tool to monitor network nodes.
        Currently supports ping(icmp), Http: Get and Post.

        To get started:
        'networkmonitor --config "demo.yaml" --newconfig'

    """

    # Pass all the requested info into the interface
    cfg = IConfig(config, newconfig)


    # Once interfaces has been made, we will send them to the CLI worker class
    cli = CLI(cfg)

    # Check if NewConfig was requested
    cli.NewConfig()
        
    main = uiMain(cfg)
    main.Start()

if __name__ == "__main__":
    init()