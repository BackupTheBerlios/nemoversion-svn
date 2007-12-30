import commands

class Command(object):
    def __init__(self):
        self.output = None
        self.__file = None
        
    def outputFormatedAsDict(self):
        return {"status":self.output[0], "output":self.output[1]}
    
    def getFile(self):
        return self.__file.get_uri()[7:]
    
    def setFile(self, value):
        self.__file = value
    
    file = property(getFile, setFile)
    
class AddCommand(Command):
    def execute(self, file):
        self.file = file
        self.output = commands.getstatusoutput("svn add " + self.file)
        return self.outputFormatedAsDict()

class RemoveCommand(Command):
    def execute(self, file):
        self.file = file
        self.output = commands.getstatusoutput("svn rm " + self.file)
        return self.outputFormatedAsDict()

class StatusCommand(Command):
    def execute(self, file):
        self.file = file
        self.output = commands.getstatusoutput("svn status " + self.file)
        return self.outputFormatedAsDict()