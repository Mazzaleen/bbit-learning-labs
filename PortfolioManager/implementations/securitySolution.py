import os
import sys

modulepath = os.path.abspath('..')
if modulepath not in sys.path:
    sys.path.append(modulepath)

 
from interfaces.securityInterface import securityInterface

class security(securityInterface):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name
        
    def getName(self) -> str:
        return self.name