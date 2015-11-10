import os
import re

from utils.pluginProvider import PluginProvider
from utils.command import Command
from plugins.basePlugin import BasePlugin

class CorePlugin(PluginProvider, BasePlugin):
    name = 'Core'

    commandPatterns = {
        'exit': "^(exit|quit|:q)",
        'help': "^(help|man|-h)",
        'test': "^test",
        'info': "^(info|who are you)",
    }

    def processCommand(self, command):
        return super(CorePlugin, self).processCommand(command)

    def info(self):
        print "I'm a bot, yo!"

    def help(self):
        print "available commands: "
        for plugin in PluginProvider.plugins:
            print plugin.commandPatterns

    def test(self):
        # create a osx notification
        title = "hello world"
        body = self.inputString
        os.system(
            "osascript -e 'display notification \"" +
            body +
            "\" with title \"" +
            title +
            "\"'"
        )

    def exit(self):
        exit()
