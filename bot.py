from parser import *

class Bot:

    def __init__(self):
        print "Hello, i am a bot."

    def __del__(self):
        print "Good bye"

    def start(self):
        parser = Parser()

        while True:
            input = raw_input(">> ")
            command = parser.parseCommand(input)
            command.execute()

bot = Bot()
bot.start()
