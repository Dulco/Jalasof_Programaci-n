
from contextlib import nullcontext
from ctypes import sizeof
from itertools import chain

class Element:
    content = ""

    def __init__(self, content) -> None:
        self.content = content
    
    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content


class MyList:

    def __init__(self, size) -> None:
        self.index = 0
        self.element = [None] * size;

    def get_index(self):
        return self.index

    def add(self, element):
        self.element[self.index] = element
        self.index += 1

    def update(self, index, element):
        self.element[index] = element

    def forList(self):
        for i in self.element:
            print(i.get_content())

    def __str__(self):
        global chain
        global cont
        cont=0
        chain= '['
        for i in self.element:
            cont+=1
            chain=chain+str(i.get_content())
            if cont<len(self.element):
                chain=chain+', '
        return chain+']'

class Main:

    def run():
        
        element1 = Element("Object 1")
        list = MyList(4)
        list.add(element1)
        element2 = Element("Object 2")
        element3 = Element("Object 3")
        element4 = Element("Object 4")
        list.add(element2)
        list.add(element3)
        list.add(element4)
        list.update(0, element3)
        list.forList()
        print(list)


    if __name__ == "__main__":
        run()