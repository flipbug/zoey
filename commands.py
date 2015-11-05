import webbrowser
import os
import re
from patterns import *

class Command:

    inputString = ""

    def __init__(self, inputString):
        self.inputString = inputString

    def execute(self):
        raise NotImplementedError()

class ExitCommand(Command):
    def execute(self):
        exit()

class UnknownCommand(Command):
    def execute(self):
        print "I don't understand."

class InfoCommand(Command):
    def execute(self):
        print "I'm a bot, yo!"

class HelpCommand(Command):
    def execute(self):
        print "available commands: "
        print PATTERNS.keys()

class VimeoCommand(Command):
    def execute(self):
        print "there you go."
        url = "https://vimeo.com/channels/staffpicks"
        webbrowser.open(url)

class SpeakCommand(Command):
    def execute(self):
        os.system("say -v vicki \"bleep blop i'm a bot!\"")

class SingCommand(Command):
    def  execute(self):
         os.system("say -v cellos \"Doo da doo da dum dee dee doodly doo dum \
            dum dum doo da doo da doo da doo da doo da doo da doo\"")

class ItunesCommand(Command):
    def execute(self):
        if re.search("play", self.inputString):
            self.playMusic()
        elif re.search("stop", self.inputString):
            self.pauseMusic()
        elif re.search("next", self.inputString):
            self.nextTrack()
        elif re.search("previous", self.inputString):
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

class TestCommand(Command):
    def execute(self):
        # create a osx notification
        title = "hello world"
        body = self.inputString
        os.system("osascript -e 'display notification \"" + body + "\" with title \"" + title + "\"'")
