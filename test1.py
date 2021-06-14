import subprocess
from termcolor import cprint
# from pyfiglet import figlet_format


logo = 'Git-Commands'


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash.\n''' + color.END


def run(*args):
    return subprocess.check_call(['git'] + list(args))

def commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")


def branch():
    br = 'master'
    br = 'main'
    
    choice = input("\nDo you want to push the branch right now to GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("push", "-u", "origin", br)

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


def pull():
    print("\nPulls changes from the current folder if *.git is initialized.")

    choice = input("\nDo you want to pull the changes from GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("pull")

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")

def merge():
    branch = input("\nType in the name of your branch: ")
    br = f'{branch}'

    run("merge", br)

def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info + "\n")

    choices = 'clone, commit, branch, pull, fetch, merge, reset, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "commit":
        commit()

    elif choose_command == "branch":
        branch()

    elif choose_command == "pull":
        pull()

    elif choose_command == "merge":
        merge()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


if __name__ == '__main__':
    main()