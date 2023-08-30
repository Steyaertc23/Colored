colors = {'red':'\033[0;31m', 'green':'\033[0;32m', 'brown':'\033[0;33m', 'blue':'\033[0;34m', 'purple':'\033[0;35m', 'cyan':'\033[0;36m', 'gray':'\033[0;37m', 'grey':'\033[0;37m', 'light_red':'\033[1;31m', 'lime':'\033[1;32m', 'yellow':'\033[1;33m'}

styles = {'bold':'\033[1m', 'faint':'\033[2m', 'italic':'\033[3m', 'underline':'\033[4m','blink':'\033[5m', 'negative':'\033[7m',"strikethrough":"\033[9m"}

def cprint(printed:str, color:str, style:str|None=None):
    reset = '\033[0m'
    if not color in colors.keys():
        raise ValueError(f"Unknown Color '{color}'")
    if not style in styles.keys() or style == None:
        raise ValueError(f"Unknown Style {style}")
    if style:
        print(f"{colors[color]}{styles[style]}{printed}", end=f"{reset}\n")
    else:
        print(f"{colors[color]}{printed}", end=f"{reset}\n")
