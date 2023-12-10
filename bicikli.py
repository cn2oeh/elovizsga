
from abc import ABC, abstractmethod

class Bicikli(ABC):

    def __init__(self, tipus, ar, allapot):
        print('típus, ár, állapot')
        pass


class OrszagutiBicikli(Bicikli):
    print('Ez egy országúti bicikli')


class HegyiBicikli(Bicikli):
    print('Ez egy hegyi bicikli')


my_bicikli = Bicikli('kék', 100, 'van')
