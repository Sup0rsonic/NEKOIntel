from lib.outputlib import *
from lib.help import *

# Please don't check the lib.help module.
# Or you're going to have a bad, bad day.
help_modules = {
    'chain': HELP_CHAIN,
    # What the fuck?
    'help': HELP_HELP
}

# The main class of HelpLib.
class HelpLib:
    def __init__(self):
        pass

    # Parses the help command into array.
    def parse_help(self, help_cmd):
        cmd = help_cmd.strip(' ').split()
        if not len(cmd):
            help(help_modules['help'])
        elif cmd[0] not in help_modules.keys():
            error(['Command not found in help.', '在帮助中未找到该命令。'])
            return
        elif len(cmd) == 1:
            help(help_modules[cmd[0]])
        elif len(cmd) > 1:
            if type(help_modules[cmd[0]]) == str:
                help(help_modules[cmd[0]])
            else:
                help(help_modules[cmd[0]][cmd[1]])
        else:
            # When a "?" occurs, it doesn't mean if there's a problem,
            # it's more about "what the fuck is wrong with you?".
            # 当我打出一个问号，并不是我有问题，而是你多少有点大病。
            warning(['?', '?'])
        return



