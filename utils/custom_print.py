from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def success(message: str):
    print(Fore.GREEN + f"✔ {message}" + Style.RESET_ALL)


def error(message: str):
    print(Fore.RED + f"✖ {message}" + Style.RESET_ALL)


def warning(message: str):
    print(Fore.YELLOW + f"⚠ {message}" + Style.RESET_ALL)


def info(message: str):
    print(Fore.CYAN + f"ℹ {message}" + Style.RESET_ALL)




