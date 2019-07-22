
import click
from click.testing import CliRunner
import networkmonitor

def test_flag_config():
    @click.command()
    @click.argument('config')
    def cfg(config):
        click.echo(config)

    runner = CliRunner()
    res = runner.invoke(cfg, ['work.json'])
    #assert res.exit_code = 0
    print(res)