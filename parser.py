import re
from patterns import *
from commands import *

class Parser:

    def parseCommand(self, input):
        for key, pattern in PATTERNS.iteritems():
            if re.match(pattern, input, re.I):
                return self.createCommandFromString(key)
        return UnknownCommand()

    def createCommandFromString(self, string):
        commandModule = __import__("command")
        className = string.capitalize() + "Command"
        return getattr(commandModule, className)()
