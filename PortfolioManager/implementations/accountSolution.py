from ast import List
import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.accountInterface import accountInterface
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable

class accountInterface():
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.accountName = accountName
        self.positions = positions

    def getName(self) -> str:
        return self.accountName

    def getAllPositions(self) -> Iterable[positionInterface]:
        return List(self.positions.values())

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        #querying of positions with a set of securitynames and security objects
        
        query_to_positions = {}
          
        for security_key in securities:
            if isinstance(security_key,securityInterface) and security_key.getName in self.positions:
                query_to_positions[security_key] = self.positions[security_key.getName]
            elif security_key in self.positions:
                query_to_positions[security_key] = self.positions[security_key.getName]
        return query_to_positions 

    def addPositions(self, positions: Set[positionInterface]) -> None:
        #Allow for positions to be added to the account with a set of position objects.
        # Incoming positions should update existing positions
        
        for p in positions:
            if p.getSecurity().getName() in self.positions:
                self.positions[p.getSecurity().getName()].setPositions(p.getPosition())
            else:
                self.positions[p.getSecurity().getName()] = p
    def removePositions(self, securities: Set) -> None:
        #Allow for the removal of positions from the 
        # account with a set of security names/security objects. 
        # Securities not in the account should be ignored.
        
        for s in securities:
            if isinstance(s,securityInterface):
                self.positions.pop(s.getName())
            else:
                self.positions.pop(s)
                