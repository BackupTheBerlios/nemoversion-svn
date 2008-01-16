class FileInfo:
    """
    dir(aFileInfoInstance) return:
    ['__class__', '__cmp__', '__delattr__', '__dict__', '__doc__', '__gdoc__',
    '__getattribute__', '__gobject_init__', '__grefcount__', '__gtype__',
    '__hash__', '__init__', '__module__', '__new__', '__reduce__',
    '__reduce_ex__', '__repr__', '__setattr__', '__str__',
    'add_emblem', 'add_string_attribute', 'chain', 'connect','connect_after',
    'connect_object', 'connect_object_after', 'disconnect', 'disconnect_by_func',
    'emit', 'emit_stop_by_name', 'freeze_notify', 'get_data', 'get_mime_type',
    'get_name', 'get_parent_uri', 'get_properties', 'get_property',
    'get_string_attribute', 'get_uri', 'get_uri_scheme', 'get_vfs_file_info',
    'handler_block', 'handler_block_by_func', 'handler_disconnect',
    'handler_is_connected', 'handler_unblock', 'handler_unblock_by_func',
    'invalidate_extension_info', 'is_directory', 'is_gone', 'is_mime_type',
    'notify', 'props', 'set_data', 'set_properties', 'set_property',
    'stop_emission', 'thaw_notify', 'weak_ref']
    """
    
    def __init__(self, file):
        self.file = file
    
    def get_uri(self):
        return "file://" + self.file
    
class Command:
    def __init__(self, file):
        self.output = None
        self.__file = file
        
    def getFile(self):
        return self.__file.get_uri()[7:]
        
    
    