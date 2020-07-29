# 2018-2019 Programação 2 LTI
# Grupo 69
# 49187 Sofia Torres
# 50383 João Paiva

from node import *

class EdgeII(Edge):
    """ EdgeII is a subclasse of Edge"""

    def __init__(self,src,dest):
        super().__init__(src,dest)

    def gettime(self):
        """
        Requires: self an edge
        Ensures: function that calculates time taken from A to B
        """

        if self.src.getGen() == "99":
            if self.dest.getGen() == "99":
                return lambda src: 1/int(src.getPower())
            else:
                return lambda src: 2/int(src.getPower())
        if self.src.getGen() == "98":
            if self.dest.getGen() == "99":
                return lambda src: 2/int(src.getPower())
            else:
                return lambda src: 2/int(src.getPower())
        if self.src.getGen() == "97":
            return lambda src: 4/int(src.getPower())
