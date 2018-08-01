import sys, os

from cliff.app import App
from plugin_cmd_mgr import PluginCommandManager


class App(App):

    def __init__(self):
        super(App, self).__init__(
            description='acli - a command line interface tool',
            version='0.1',
            command_manager=PluginCommandManager('alci'),
            deferred_help=True,
            )

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)

def main(argv=sys.argv[2:]):
    app = App()
    return app.run(argv)

if __name__ == '__main__':
    print sys.argv[0], os.getcwd()
    curdir = sys.argv[1]
    #os.chdir(curdir)
    sys.exit(main(sys.argv[2:]))