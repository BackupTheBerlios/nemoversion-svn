import commands

class Command(object):
    def __init__(self, file):
        self.output = None
        self.__file = file
        
    def outputFormatedAsDict(self):
        return {"status":self.output[0], "output":self.output[1]}
    
    def getFile(self):
        return self.__file.get_uri()[7:]
    
    #TODO: remove this shit
    def setFile(self, value):
        self.__file = value
        
    def preExecute(self):
        raise NotImplementedError
    
    def execute(self):
        self.preExecute()
        return self.outputFormatedAsDict()
    
    def __eq__(self, other):
        sameFile = other.getFile() == self.getFile()
        sameClass = other.__class__.__name__ == self.__class__.__name__
        if  sameFile and sameClass:
            return True
        return False
    
    file = property(getFile, setFile)

class AddCommand(Command):
    def preExecute(self):
        self.output = commands.getstatusoutput("svn add " + self.file)

class RemoveCommand(Command):
    def preExecute(self):
        self.output = commands.getstatusoutput("svn remove " + self.file)

class StatusCommand(Command):
    def preExecute(self):
        self.output = commands.getstatusoutput("svn status " + self.file)