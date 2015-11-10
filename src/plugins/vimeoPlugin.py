import webbrowser

from utils.actionProvider import ActionProvider
from utils.command import Command

class VimeoPlugin(ActionProvider):
    name = "Vimeo"

    commandPatterns = {
        'vimeo': "^show.*video",
    }

    def processCommand(self, command):
        print "there you go."
        url = "https://vimeo.com/channels/staffpicks"
        webbrowser.open(url)
