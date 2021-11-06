from lib.outputlib import *
import os
import sys
import time
import json
import random
import getpass

# The CMDLineController handles the user interaction experience.
# Make it MVC, Make it MVM, make it whatever.
# The user does not interact with the MainController directly. Instead of using MainController, they
#   interacts with CMDLineController, and the controller parses the command, feeds it to the maincontroller.
# In the meantime, it's a pain to integrate this much of classes in a single script, eh?


class CMDLineController:
    def __init__(self):
        debug('CMDLineController init()')
        self.chain = None
        self.dir = os.path.curdir
        self.time = time.time()
        debug('MainController load()')
        # TODO: Links to a main controller.
        self.main_controller = None
        pass

    # The main interactive method that listens from commandline and feed the data to parser.
    def interactive(self):
        debug('Entering interactive.')
        cmd = None
        while True:
            cmd = input(PS1.replace('%CHAIN%', self.chain).replace('%CWD%', self.dir))
            debug(f'CMD {cmd}')
            self.parse_commands(cmd)

    # The main cmd parser. Parses the command and feeds it to the main controller.
    def parse_commands(self, cmd):
        cmd = cmd.split(cmd)
        for item in cmd:
            item = item.strip()
            if not item:
                cmd.remove(item)

    def cd(self, dir):
        try:
            os.chdir(dir)
            self.dir = os.path.curdir
        except Exception as e:
            debug(e)
            error([f'Unable to change to directory {dir}.', f'无法切换到目录{dir}。'])
        return

    # Python 3.10 Now supports case, but my IDE doesn't recognize it.
    # Which makes the pain even stronger.
    def cmd_parser(self, cmd):
        pass

    def pass_through(self, args):
        cmd = ''
        for item in args:
            cmd += item
            cmd += ' '
        try:
            debug(f'CMD {cmd}, executing os.system().')
            os.system(cmd)
        except SystemError as e:
            error([f'Unable to execute command {cmd}, {e}.',f'无法执行命令{cmd}, {e}。'])
        return

    def splash_screen(self):
        try:
            with open(f'{os.path.dirname(os.path.abspath(__file__))}/../config.json') as fp:
                with json.load(fp) as configs:
                    with open(f'{os.path.dirname(os.path.abspath(__file__))}/../presets/{configs["splash_screen_file_name"]}').readlines() as splash_screen:
                        print(splash_screen[random.randint(0, len(splash_screen)-1)])
            ok([f'{FG_NEKOINTEL}NEKOIntel{COLOR_RESET} ver {configs["NEKOIntel_version"]} "{configs["NEKOIntel_codename"]}"', f'{FG_NEKOINTEL}猫情报{COLOR_RESET}，版本{configs["NEKOIntel_version"]}，"{configs["NEKOIntel_codename"]}"'])
            ok([f'Welcome, {str(getpass.getuser())}. All cats on deck.', f'欢迎，{str(getpass.getuser())}，所有猫猫都已就位。'])
        except json.JSONDecodeError or FileNotFoundError as e:
            error([' (=🝦 ༝ 🝦=) Splash screen file not found...', '(=🝦 ༝ 🝦=) 无法找到欢迎屏幕文件...'])

    # Sends the command to the MainController(). Scrap it.
    # I mean, I'm currently unemployed, so pretty much everything has been a pain.
    # Even now, I'm thinking about what can I do.
    def send_command(self, cmd):
        debug('CMDLINE_SEND_CMD_TO_MAIN_CTRL')
        self.main_controller.parse_commands(cmd)
        return