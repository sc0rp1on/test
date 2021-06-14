import subprocess
# from termcolor import cprint
# from pyfiglet import figlet_format

logo = 'Git-Commands'

info = 'Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash.\n'

def run(*args):
    return subprocess.check_call(['git'] + list(args))

def commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("add", "--all")
    run("commit", "-m", commit_message)
    run("push")
    # run("push", "-u", "origin", "master")

def main():
    choices = 'commit'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "commit":
        commit()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


if __name__ == '__main__':
    main()