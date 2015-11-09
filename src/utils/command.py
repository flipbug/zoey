class Command:

    _inputString = ""
    _keyword = ""
    _arguments = []

    def __init__(self, keyword, inputString):
        self.inputString = inputString
        self.keyword = keyword
        self.arguments = self.getArgumentsFromInput()

    def _getArgumentsFromInput():
        return []

    def getKeyword():
        return self.keyword

    def getArguments():
        return self.arguments
