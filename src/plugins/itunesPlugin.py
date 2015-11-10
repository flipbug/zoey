import os
import re

from utils.pluginProvider import PluginProvider
from utils.command import Command

class ItunesPlugin(PluginProvider):
    name = "Itunes"

    commandPatterns = {
        'itunes': "^(itunes|play|stop|next|previous)",
    }

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
