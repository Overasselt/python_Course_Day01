class Tool:
    def __init__(self, type, serienummer):
        self.type = type
        self.serienummer = serienummer

    def __repr__(self):
        return ' - '.join(self.__dict__.values())

# ..................................................................
if __name__ == '__main__':
    tool = []

    tool.append( Tool('Wrench', '1231231'))
    tool.append( Tool('Wrench', '3453426'))

    for Tool in tool:
        print(Tool)
