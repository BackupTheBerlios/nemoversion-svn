from nemoversion.appcontroller import factory

class NemoversionController:
    
    def __init__(self):
        pass
    
    def execute(self, file, menuid):
        fac = factory.ActionFactory()
        fac.execute(file, menuid)
