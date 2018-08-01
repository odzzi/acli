import os,re
from cliff.commandmanager import CommandManager
from cliff.command import Command


def make_cmd(cmd):
    class CmdApp(Command):
        interactive = False
        def get_description(self):
            return str(cmd['desc'])

        def get_parser(self, prog_name):
            """Return an :class:`argparse.ArgumentParser`.
            """
            if "interactive" in cmd:
                self.interactive = cmd["interactive"]
            parser = super(CmdApp, self).get_parser(prog_name)
            for para in cmd['paras']:
                parser.add_argument(para, nargs='?', default='.')
            return parser

        def take_action(self, parsed_args):
            po = os.popen(cmd['cmd'] % vars(parsed_args))
            ret_text = po.read()
            print po.name, ret_text

    return CmdApp


def loadCmds(path):
    import json
    cmds = json.load(open(path, "r"))
    return cmds


class PluginCommandManager(CommandManager):

    def load_commands(self, namespace):
        cmds = loadCmds("cmds.json")
        for cmd in cmds:
            self.add_command(cmd['name'], make_cmd(cmd))

