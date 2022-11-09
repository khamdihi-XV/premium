#!/usr/bin/python3

from os import system
try:from art.main import folder
except FileNotFoundError:exit('\n [×] Update dulu version python anda : pkg install python')
system('clear') ; system('git pull')


if __name__ == "__main__":
        try:
                __import__("main").folder()
        except Exception as e:
                exit(str(e))
