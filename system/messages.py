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
    #audios.play(r"modules\sounds\audios\main_error.mp3")


# continuation message
def continuation(msg):
    print(colorama.Fore.BLUE + msg +" ...\n" + colorama.Fore.RESET)

def user(msg):
    print(colorama.Fore.CYAN + "User: " + msg + "\n" + colorama.Fore.RESET)

def assistent(msg):
    print(colorama.Fore.MAGENTA + ")=--> " + msg + " <--=(\n" + colorama.Fore.RESET)