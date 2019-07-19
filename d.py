import click
@click.command()
@click.option('--config', default='config.json', help='Configuration file to load.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(config, name):
    """Simple program that greets NAME for a total of COUNT times."""
    count = 2
    click.echo(config)
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()