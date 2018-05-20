from abc import ABC, abstractmethod

class Item(ABC):

    __id = 0

    def __init__(self):
        type(self).__id += 1
