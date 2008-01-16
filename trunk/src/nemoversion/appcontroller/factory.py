#factories

class ActionFactory:
    
    def __init__(self):
        pass
    
    def createAction(self, file, menuid):
        """
        Create an action for a given file and menu id
        param file: a FileInfoInstance
        param menuid: an unique menuid - string
        return: an action (svn command, git command)
        """
        exec("from nemoversion.repository.svncommand import " + menuid)
        exec("retval = " + menuid + "(file)")
        return retval