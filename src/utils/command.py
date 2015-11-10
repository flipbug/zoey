class Command:

    _inputString = ""
    _keyword = ""
    _arguments = []

    def __init__(self, keyword, inputString):
        self.inputString = inputString
        self.keyword = keyword
        self.arguments = self._getArgumentsFromInput()

    def _getArgumentsFromInput(self):
        return []

    def getKeyword(self):
        return self.keyword

    def getArguments(self):
        return self.arguments
