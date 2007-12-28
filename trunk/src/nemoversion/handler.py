#main module for nemo version
import nautilus
import gconf
from nemoversion.appcontroller import factory

class NemoversionHandler(nautilus.MenuProvider, nautilus.InfoProvider):
    def __init__(self):
        self.client = gconf.client_get_default()
        self.__menuItens = []
    
    #TODO: remove
    def __showInfo(self):
        print self
    
    def __addMenuItem(self, item, description):
        """
        Add a item to menuItens (itens for file-menu and bg-menu)
        param item: menu label
        param description: menu description
        """
        menuid = 'Nemoversion::%s_item' %item.replace(' ', '_')
        item = nautilus.MenuItem(menuid, item, description)
        item.connect('activate', self.__actionFor(file, menuid), file)
        self.__menuItens.append(item)
    
    #TODO: implement factory for __actionFor        
    def __actionFor(self, file, menuid):
        """
        Dynamically get an action for the given file.
        param file: a simple python file type
        return: an activate action
        """
        actionFactory = factory.ActionFactory()
        return actionFactory.createAction(file, menuId)
        

    def get_file_items(self, window, files):
        """
        Callback function for files
        param window:
        param files: selected files
        """
        return self.__menuItens
    
    def get_background_items(self, window, file):
        """
        Callback function for directory background click
        param window:
        param file: current dir background
        """
        return self.__menuItens