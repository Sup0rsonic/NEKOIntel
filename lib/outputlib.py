from colored import fg, bg, attr
import locale

OUTPUTLIB_LANG = 1 if locale.getdefaultlocale()[0] == 'zh_CN' else 0
IS_DEBUG = 1

FG_PINK = fg('pale_violet_red_1')
FG_BLUE = fg('deep_sky_blue_1')
FG_GREEN = fg('spring_green_3b')
FG_YELLOW = fg('light_goldenrod_2b')
FG_ORANGE = fg('orange_3')
FG_RED = fg(196)
FG_CYAN = fg(122)
FG_NEKOINTEL = fg(168)

COLOR_RESET = attr('reset')

PS1 = f'{FG_NEKOINTEL}[ NEKOIntel ] {COLOR_RESET + FG_PINK} %CHAIN% {COLOR_RESET} $ '

def info(content):
    print(f'{FG_BLUE}[{" 信息 " if OUTPUTLIB_LANG else " INFO "}] {COLOR_RESET + content[OUTPUTLIB_LANG]}')
    return

def ok(content):
    print(f'{FG_GREEN}[{" 成功 " if OUTPUTLIB_LANG else "  OK  "}] {COLOR_RESET + content[OUTPUTLIB_LANG]}')
    return

def warning(content):
    print(f'{FG_ORANGE}[{" 警报 " if OUTPUTLIB_LANG else " WARN "}] {COLOR_RESET + content[OUTPUTLIB_LANG]}')
    return

def error(content):
    print(f'{FG_RED}[{" 错误 " if OUTPUTLIB_LANG else " ERRR "}] {COLOR_RESET + content[OUTPUTLIB_LANG]}')
    return

def help(content):
    print(f'{FG_BLUE}[{" 帮助 " if OUTPUTLIB_LANG else " HELP "}] {COLOR_RESET + content[OUTPUTLIB_LANG]}')
    return

def critical(content, exit_code=255):
    print(f'{FG_YELLOW}[{" 致命 " if OUTPUTLIB_LANG else " CRIT "}] {COLOR_RESET + content[OUTPUTLIB_LANG]}')
    if exit_code:
        exit(int(exit_code))
    return

def debug(content):
    if IS_DEBUG:
        print(f'{FG_BLUE}[{" 调试 " if OUTPUTLIB_LANG else " DEBG "}] {COLOR_RESET + content[OUTPUTLIB_LANG]}')
    return

def prompt(content):
    return input(f'{FG_PINK}[{" 输入 " if OUTPUTLIB_LANG else " INPT "}]{COLOR_RESET}{content[OUTPUTLIB_LANG]}: ')

def test():
    test_string = ['NEKOIntel Output test', '猫情报 输入测试' ]
    info(test_string)
    ok(test_string)
    warning(test_string)
    error(test_string)
    critical(test_string, 0)
    debug(test_string)
    prompt(['OwO', 'QwQ'])


if __name__ == '__main__':
    OUTPUTLIB_LANG = 1
    test()