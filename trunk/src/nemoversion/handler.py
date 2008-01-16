#main module for nemo version
import nautilus
import gconf
from nemoversion import appcontroller

class NemoversionHandler(nautilus.MenuProvider, nautilus.InfoProvider):
    def __init__(self):
        self.client = gconf.client_get_default()
        self.__menuItens = []
    
    #TODO: remove
    def __showInfo(self):
        print self
    
    def __addMenuItem(self, file, item, description):
        """
        Add a item to menuItens (itens for file-menu and bg-menu)
        param file: a FileInfo instance
        param item: menu label/id
        param description: menu description
        """
        menuid = 'Nemoversion::%s' %item.replace(' ', '_')
        item = nautilus.MenuItem(menuid, item, description)
        item.connect('activate', self.genericCallback(file, menuid), file)
        self.__menuItens.append(item)
    
    def genericCallback(self, file, menuid):
        """
        Execute an action for the given file.
        param file: a FileInfo instance
        return: an activate action
        """
        cntrl = appcontroller.NemoversionController()
        return cntrl.execute(file, menuid)

    def get_file_items(self, window, files):
        """
        Callback function for files
        param window:
        param files: selected files (list of FileInfo instances)
        """
        return self.__menuItens
    
    def get_background_items(self, window, file):
        """
        Callback function for directory background click
        param window:
        param file: current dir background
        """
        return self.__menuItens