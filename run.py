#!/usr/bin/python3

from os import system
from art.main import folder
system('clear')


if __name__ == "__main__":
        try:
                __import__("art").folder()
        except Exception as e:
                exit(str(e))
