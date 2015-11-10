import re
from utils.command import Command

class Parser:
    commandPatterns = {}

    def __init__(self, patterns):
        self.commandPatterns = patterns

    def getCommandFromInput(self, input):
        for keyword, pattern in self.commandPatterns.items():
            if re.match(pattern, input, re.I):
                return Command(keyword, input)
        raise NotImplementedError
