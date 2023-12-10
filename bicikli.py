
from abc import ABC, abstractmethod

class Bicikli(ABC):

    def __init__(self, tipus, ar, allapot):
        print('típus, ár, állapot')
        pass

my_bicikli = Bicikli('kék', 100, 'van')