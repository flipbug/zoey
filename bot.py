import sys
from parser import *

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

        # don't loop if argument is already defined
        if self.input:
            command = parser.parseCommand(self.input)
            command.execute()
        else:
            while True:
                input = raw_input(">> ")
                command = parser.parseCommand(input)
                command.execute()

input = ' '.join(sys.argv[1:])
bot = Bot(input)
bot.start()
