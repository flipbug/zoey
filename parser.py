import re
from patterns import *
from commands import *

class Parser:

    def parseCommand(self, input):
        for key, pattern in PATTERNS.iteritems():
            if re.match(pattern, input, re.I):
                return self.createCommandFromString(key, input)
        return UnknownCommand(input)

    def createCommandFromString(self, string, originalInput):
        commandModule = __import__("commands")
        className = string.capitalize() + "Command"
        return getattr(commandModule, className)(originalInput)
