import webbrowser

from actionProvider import ActionProvider
from command import Command

class VimeoPlugin(ActionProvider):
    name = "Vimeo"

    def processCommand(self):
        print "there you go."
        url = "https://vimeo.com/channels/staffpicks"
        webbrowser.open(url)
