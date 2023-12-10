
from abc import ABC, abstractmethod

class Bicikli(ABC):

    def __init__(self, tipus, ar, allapot):
        print('típus, ár, állapot')
        pass


class OrszagutiBicikli(Bicikli):
    print('Ez egy országúti bicikli')


class HegyiBicikli(Bicikli):
    print('Ez egy hegyi bicikli')


class Kolcsonzo:
    def __init__(self, biciklik:[Bicikli], kolcsonzonev: str):
        self.biciklik = biciklik
        self.kolcsonzonev = kolcsonzonev

    def __str__(self):
        return f"A kölcsönző neve {self.kolcsonzonev}."


my_biciklik = [Bicikli("Országúti bicikli", 100000, "jó állapotú" ), Bicikli("Hegyi bicikli",150000, "lestrapált")]
my_kolcsonzo = Kolcsonzo([my_biciklik],"Tekergő")
print(my_kolcsonzo)

#my_bicikli = Bicikli('kék', 100, 'van')


