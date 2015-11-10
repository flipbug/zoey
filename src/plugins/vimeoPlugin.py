import webbrowser

from utils.pluginProvider import PluginProvider
from utils.command import Command

class VimeoPlugin(PluginProvider):
    name = "Vimeo"

    commandPatterns = {
        'vimeo': "^show.*video",
    }

    def processCommand(self, command):
        print "there you go."
        url = "https://vimeo.com/channels/staffpicks"
        webbrowser.open(url)
