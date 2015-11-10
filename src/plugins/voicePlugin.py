import os

from utils.actionProvider import ActionProvider
from utils.command import Command
from plugins.basePlugin import BasePlugin


class VoicePlugin(ActionProvider, BasePlugin):
    name = "Voice"

    commandPatterns = {
        'speak': "^speak",
        'sing': "^sing",
    }

    def processCommand(self, command):
        return super(VoicePlugin, self).processCommand(command)

    def speak(self):
        os.system("say -v vicki \"bleep blop i'm a bot!\"")

    def sing(self):
         os.system("say -v cellos \"Doo da doo da dum dee dee doodly doo dum \
            dum dum doo da doo da doo da doo da doo da doo da doo\"")
