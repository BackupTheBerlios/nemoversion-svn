#main module for nemo version
import nautilus
import gconf

class NemoversionHandler(nautilus.MenuProvider, nautilus.InfoProvider):
    def __init__(self):
        self.client = gconf.client_get_default()
        self.__menuItens = []
    
    def __addMenuItem(self, item, description):
        menuid = 'Nemoversion::%s_item' %item.replace(' ', '_')
        item = nautilus.MenuItem(menuid, item, description)
        item.connect('activate', self.menu_activate_cb, file)
        self.__menuItens.append(item)
        
    #TODO: implement
    def menu_activate_cb(self, menu, file):
        pass
    
    #TODO: implement    
    def menu_background_activate_cb(self, menu, file):
        pass

    #TODO: implement
    def get_file_items(self, window, files):
        pass
    
    #TODO: implement
    def get_background_items(self, window, file):
        pass