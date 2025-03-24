import os

class ui:
    ENDC = '\033[0m'
    terminal_size = lambda: os.get_terminal_size().columns
    HEADER = lambda txt:f'\033[95m{txt}{ui.ENDC}'
    OKBLUE = lambda txt:f'\033[94m{txt}{ui.ENDC}'
    OKCYAN = lambda txt:f'\033[96m{txt}{ui.ENDC}'
    OKGREEN = lambda txt:f'\033[92m{txt}{ui.ENDC}'
    WARNING = lambda txt:f'\033[93m{txt}{ui.ENDC}'
    BOLD = lambda txt:f'\033[1m{txt}{ui.ENDC}'
    UNDERLINE = lambda txt:f'\033[4m{txt}{ui.ENDC}'
    FAIL = lambda txt:f'\033[91m{txt}{ui.ENDC}'

    CHECK = '✅'
    PENCIL = "🖉"
    CAUTION = '⚠️'
    FAILED = '❌'

    @staticmethod
    def doge():
        parts = [
            "=================",
            "|     __      _ |",
            "|   o'')}____// |",
            "|   `_/      )  |",
            "|   (_(_/-(_/   |",
            "=================",
            "~ Pure Michigan ~"
        ]
        for txt in parts: print(txt.center(ui.terminal_size(), "`"))

    @staticmethod
    def print(txt,left:bool=False,right:bool=False,center:bool=False,spacer:str=' '):
        if left:
            print(txt.ljust(ui.terminal_size(), spacer))
        elif right:
            print(txt.rjust(ui.terminal_size(), spacer))
        elif center:
            print(txt.center(ui.terminal_size(), spacer))
        else:
            print(txt)

    @staticmethod
    def line(num:int=1): 
        if num > 1:
            for _ in range(num):ui.print("-"*ui.terminal_size())
        else:
            ui.print("-"*ui.terminal_size())

    @staticmethod
    def warn(txt:str='',left:bool=False,right:bool=False,center:bool=False):
        self.print(ui.WARNING(txt),left,right,center)

    @staticmethod
    def fail(txt:str=''):
        self.print(ui.WARNING(txt),left,right,center)

    @staticmethod
    def header(txt:str=''):
        print("#"*ui.terminal_size())
        print(txt.center(ui.terminal_size(), " "))
        print("#"*ui.terminal_size())
    
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')