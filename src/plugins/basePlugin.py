from utils.command import Command

class BasePlugin:
    commandPatterns = {}

    def processCommand(self, command):
        for keyword in self.commandPatterns:
            if keyword is command.getKeyword():
                getattr(self, keyword)()
                return True
        return False
