import os

def main():
    if input("Run installer? y/n ") != "y":
        return
    os.system('pip install discord.py')

main()