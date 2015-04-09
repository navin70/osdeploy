from keystone import *

class osdeploy(keystone):
    def install(self):
        k = keystone()
        print k.project_name
        
o = osdeploy()
o.install()
