#! /usr/bin/python3

class mipila:
    """
    TAD pila sobre la class lista"""

    # __h = 0
    __data = []
    __hmax = None

    def __init__(self, hmax=10):
        # self.__data = []
        self.__hmax = hmax

    def __str__(self) -> str:
        answ = "<"
        answ += f"{self.h()} de {self.__hmax}, {self.__data}"
        if self.esLlena(): answ += " LLENA"
        answ += ">"
        return answ

    def push(self,algo):
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

    # mp = mipila()
    # print(mp)

    mp3 = mipila(20)  # tested: default, 8, 4, 3, 2, 1, 0 OK
    print(mp3)

    mp3.push(11)
    print(mp3)

    mp3.push(33)
    print(mp3)

    mp3.push(22)
    print(mp3)

    mp3.push("doblada")
    print(mp3)

    # mp3.drop()
    # print(mp3)

    item = mp3.pop()
    print(mp3, mp3.esLlena(), "item: ", item)

    item = mp3.pop()
    print(mp3, mp3.esLlena(), "item: ", item)

    item = mp3.pop()
    print(mp3, mp3.esLlena(), "item: ", item)

    item = mp3.pop()
    print(mp3, mp3.esLlena(), "item: ", item)

    mp3.push(None)
    print(mp3)

    mp3.push("algo mas")
    print(mp3)

    mp3.push(None)
    print(mp3)


