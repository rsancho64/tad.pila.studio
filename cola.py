#! /usr/bin/python3

class micola:
    """
    TAD cola sobre la class lista"""

    __data = []
    __hmax = None

    def __init__(self, hmax=10):
        # self.__data = []
        self.__hmax = hmax

    def __str__(self) -> str:
        answ = "<"
        answ += f"{self.h()} de {self.__hmax}, {self.__data}"
        if self.esLlena():
            answ += " LLENA"
        answ += ">"
        return answ

    def push(self, algo):
        if not self.esLlena():
            self.__data.append(algo)

    def pop(self):
        try:
            return self.__data.pop()
        except IndexError:
            return None

    def esLlena(self) -> bool:
        if len(self.__data) == self.__hmax:
            return True
        return False

    def esVacia(self) -> bool:
        return not self.esLlena()

    def h(self) -> int:
        return len(self.__data)

    def drop(self):
        self.__data = []


if __name__ == "__main__":

    mc = []
    print(mc) # []
  
    mc.append('11')
    print(mc) # ['11']

    mc.append('22')
    print(mc) # ['11', '22']

    mc.append('33')
    print(mc) # ['11', '22', '33']

    print(mc.pop(0)) # 11
    print(mc) # ['22', '33']

    print(mc.pop(0)) # 22
    print(mc) # ['33']
    
    print(mc.pop(0)) # 33
    print(mc)  # []   
