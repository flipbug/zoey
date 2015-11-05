import webbrowser
from patterns import *

class Command:
    def execute(self):
        raise NotImplementedError()

class ExitCommand(Command):
    def execute(self):
        exit()

class UnknownCommand(Command):
    def execute(self):
        print "I don't understand"

class InfoCommand(Command):
    def execute(self):
        print "I'm a bot, yo!"

class HelpCommand(Command):
    def execute(self):
        print "available commands: "
        print PATTERNS.keys()

class VimeoCommand(Command):
    def execute(self):
        print "here you go"
        url = "https://vimeo.com/channels/staffpicks"
        webbrowser.open(url)
