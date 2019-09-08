
import click

from networkmonitor.src.configuration import *

class CLI:
    """
    This is the working class that helps with all the CLI flags that are passed to the application.
    """
    def __init__(self, cfg: IConfig):
        self.config: IConfig = cfg
        pass

    def NewConfig(self):
        """
        This will handle the generation of new config files on request.
        """

        if self.config.argNewConfig == True:        
            # Check if the requested --config is valid
            if self.config.argPathConfig.endswith('.yaml'):
                y = YamlConfig(self.config)
            elif self.config.argPathConfig.endswith('.json'):
                y = JsonConfig(self.config)
            else:
                pass 

            cc = ContextConfig(y)
            cc.NewConfig()
            click.echo("New file has been made!")
        pass
