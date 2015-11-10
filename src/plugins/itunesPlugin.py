import os
import re

from utils.actionProvider import ActionProvider
from utils.command import Command

class ItunesPlugin(ActionProvider):
    name = "Itunes"
    
    commandPatterns = {
        'exit': "^(exit|quit|:q)",
        'help': "^(help|man|-h)",
        'info': "^(info|who are you)",
    }

    def __init__(self, request, *args, **kwargs):
        pass

    def processCommand(self, command):
        if re.search("play", command.keyWord):
            self.playMusic()
        elif re.search("stop", command.keyWord):
            self.pauseMusic()
        elif re.search("next", command.keyWord):
            self.nextTrack()
        elif re.search("previous", command.keyWord):
            self.prevTrack()

    def playMusic(self):
        print "enjoy"
        os.system("osascript -e 'Tell application \"iTunes\" to play'")

    def pauseMusic(self):
        os.system("osascript -e 'Tell application \"iTunes\" to pause'")

    def nextTrack(self):
        os.system("osascript -e 'Tell application \"iTunes\" to play next track'")

    def prevTrack(self):
        os.system("osascript -e 'Tell application \"iTunes\" to play previous track'")
