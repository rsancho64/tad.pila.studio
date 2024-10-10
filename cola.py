#! /usr/bin/python3

class micola:
    """
    TAD cola sobre la class lista"""

    __data = []
    __hmax = None # todo refact: lmax

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

    c = []   # TODO: use mc = micola()
    print(c) # []
  
    c.append('welo')
    print(c) # ['welo']

    c.append('papa')
    print(c) # ['welo', 'papa']

    c.append('hijo')
    print(c) # ['welo', 'papa', hijo]

    print(c.pop(0)) # 11
    print(c) # ['papa', hijo]

    print(c.pop(0)) # papa
    print(c) # [hijo]
    
    print(c.pop(0)) # 33
    print(c)  # []   
