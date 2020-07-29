# 2018-2019 Programação 2 LTI
# Grupo 69
# 49187 Sofia Torres
# 50383 João Paiva

from node import *


class NodeII(Node):

    def __init__(self, id, name, power, gen):
        """
        id, name, power, gen: as str
        """
        super().__init__(name)
        self._id = id
        self._power = power
        self._gen = gen

    def getId(self):
        return self._id

    def setId(self):
        return self._id

    def getPower(self):
        return self._power

    def setPower(self):
        return self._power

    def getGen(self):
        return self._gen

    def setGen(self):
        return self._gen


    def connected(self,other):
        """
        other: other is a nodeII object

        """
        gensrc = self.getGen()
        gendest = other.getGen()
        if gensrc == "99" and gendest in ["99", "98"] or \
            gensrc == "98" and gendest in ["99", "98"] or \
                gensrc == "97" and gendest == "97":
            return True
        else:
            return False

    def disconnect97(self,other):
        gensrc = self.getGen()
        gendest = other.getGen()
        if gensrc == "97" and gendest in ["98", "99"] \
                or gensrc in ["98", "99"] and gendest == "97":
            return True
        return False


    def __repr__(self):
        return self.name

