
import click

from networkmonitor.src.configuration import IConfig, YamlConfig

from networkmonitor.tui import uiMain

#@click.command()
#def cfg():
#    click.echo(f"Do the thing {cfg}!")

@click.command()
@click.option('--config', default='config.json', help='json configuration file to load')
@click.option('--newconfig', default=False, help='Generates a new configuration file')
def init(config:str, newconfig:bool):
    """
        NetworkMonitor is a curses tool to monitor network nodes.
        Currently supports ping(icmp), Http: Get and Post.

        To get started:
        'networkmonitor --config "demo.json" --newconfig'

    """

    
    click.echo(f"config:{config}")


    # Check requirements for --newconfig
    if newconfig == True:
        click.echo(f"newConfig: {newconfig}")
        genNew:bool = False

        # Check if the requested --config is valid
        if config.__eq__("config.json"):
            pass
        elif config.__eq__("config.yaml"):
            pass
        else:
           pass 

        
    if config.__eq__("config.json") or config.__eq__("config.yaml"):
        if newconfig == True:
            print("Invalid commands.  To generate a new configuration run the following flags:")
            print(" --config 'newConfig.yaml' --newconfig")
            print('This will generate a new configuration file for you with the name you requested.')
            exit()


    main = uiMain(config)
    main.Start()

if __name__ == "__main__":
    init()