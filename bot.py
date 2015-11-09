import sys

from actionProvider import ActionProvider
from plugins import corePlugin, itunesPlugin, VimeoPlugin, VoicePlugin
from command import Command
from parser import Parser

class Bot:

    input = ""

    def __init__(self, input):
        if input:
            self.input = input
        else:
            print "Hello, i am a bot."

    def __del__(self):
        if not input:
            print "Good bye"

    def start(self):
        parser = Parser()

        for p in ActionProvider.plugins:
            print p.name

        # don't loop if an input is already defined
    """
            if self.input:
                self.dispatchCommand(parser.parseCommand(self.input))
            else:
                while True:
                    input = raw_input(">> ")
                    self.dispatchCommand(parser.parseCommand(input))
    """
    def dispatchCommand(self, command):
        pass


input = ' '.join(sys.argv[1:])
bot = Bot(input)
bot.start()
