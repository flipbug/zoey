import os

from actionProvider import ActionProvider
from command import Command

class VoicePlugin(ActionProvider)
    name = "Voice"
    
    def processCommand(self):
        pass

    def speak(self):
        os.system("say -v vicki \"bleep blop i'm a bot!\"")

    def sing(self):
         os.system("say -v cellos \"Doo da doo da dum dee dee doodly doo dum \
            dum dum doo da doo da doo da doo da doo da doo da doo\"")
