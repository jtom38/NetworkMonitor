
import click


@click.command()
@click.option(
    '-c', '--config',
    is_flag=True,
    help=u"Lets you define what configuration file that will be loaded. "
        u'Default file is config.json'
)

def main(config:str=''):
    if config == "":
        print("nothing found")

    pass


if __name__ == "__main__":
    main()
    pass
