C_RED = '\033[91m'
C_GREEN = '\33[32m'
C_LIGHT_GRAY = '\033[37m'
C_YELLOW = '\033[93m'
C_END = '\033[0m'


def write(msg: str):
    replaced_msg = msg.replace('<', C_YELLOW).replace('>', C_LIGHT_GRAY)
    print(f"{C_RED}[{C_GREEN}AoC{C_RED}]{C_END} {C_LIGHT_GRAY}{replaced_msg}")
