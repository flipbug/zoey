import os
import re

from actionProvider import ActionProvider
from command import Command

class CorePlugin(ActionProvider):
    name = 'Core'

    def __init__(self, request, *args, **kwargs):
        pass

    def processCommand(self, command):
        pass

    def info():
        print "I'm a bot, yo!"

    def help():
        print "available commands: "

    def test():
        # create a osx notification
        title = "hello world"
        body = self.inputString
        os.system("osascript -e 'display notification \"" + body + "\" with title \"" + title + "\"'")

    def unknownCommand():
        print "I don't understand."

    def exit():
        exit()
