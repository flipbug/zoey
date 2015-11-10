import sys

from utils.command import Command
from utils.parser import Parser
from utils.actionProvider import ActionProvider

from plugins import corePlugin, itunesPlugin, vimeoPlugin, voicePlugin

class Bot:

    input = ""
    welcomeMessage = "Hello, i am a bot."
    quitMessage = "Good bye"
    commandNotFoundMessage = "I don't know what you mean"

    _parser = None

    def __init__(self, input):
        patterns = self.fetchCommandPatterns()
        self._parser = Parser(patterns)
        if input:
            self.input = input
        else:
            print self.welcomeMessage

    def __del__(self):
        if not input:
            print self.quitMessage

    def fetchCommandPatterns(self):
        commandPatterns = {}
        for plugin in ActionProvider.plugins:
            if hasattr(plugin, 'commandPatterns'):
                commandPatterns.update(plugin.commandPatterns)
        return commandPatterns

    def start(self):
        if self.input:
            self.dispatchCommand(self.input)
        else:
            self.beginMainLoop()

    def beginMainLoop(self):
        while True:
            input = raw_input(">> ")
            self.dispatchCommand(input)

    def dispatchCommand(self, input):
        try:
            command = self._parser.getCommandFromInput(input)
            for plugin in ActionProvider.plugins:
                if command.getKeyword() in plugin.commandPatterns:
                    pluginObj = plugin()
                    return pluginObj.processCommand(command)
        except NotImplementedError:
            print commandNotFoundMessage
            return False

input = ' '.join(sys.argv[1:])
bot = Bot(input)
bot.start()
