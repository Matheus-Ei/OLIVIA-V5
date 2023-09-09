# Import Libraries
import colorama
import modules.sounds.audios as audios


# waring message
def waring(msg):
    print(colorama.Fore.YELLOW + "==> "+ msg +" <==" + colorama.Fore.RESET)

# informative message
def informative(msg):
    print(colorama.Fore.GREEN + "--> "+ msg +" <--" + colorama.Fore.RESET)

# error message
def error(msg):
    print(colorama.Fore.RED + "#####==-> "+ msg +" <-==#####" + colorama.Fore.RESET)

# continuation message
def continuation(msg):
    print(colorama.Fore.BLUE + msg +" ...\n" + colorama.Fore.RESET)

# user message
def user(msg):
    print(colorama.Fore.CYAN + "User: " + msg + "\n" + colorama.Fore.RESET)

# assistent message
def assistent(msg):
    print(colorama.Fore.MAGENTA + ")=--> " + msg + " <--=(\n" + colorama.Fore.RESET)