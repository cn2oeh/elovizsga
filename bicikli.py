from abc import ABC, abstractmethod
from datetime import datetime


class Bicikli(ABC):
    def __init__(self, sorszam, ar):
        self.sorszam = sorszam
        self.ar = ar
        self.kolcsonzesek = []

    def szabad_e(self, kezdo_datum, veg_datum):
        for kolcsonzes in self.kolcsonzesek:
            if not (kolcsonzes['veg_datum'] < kezdo_datum or kolcsonzes['kezdo_datum'] > veg_datum):
                return False
        return True

    def foglal(self, kezdo_datum, veg_datum):
        if self.szabad_e(kezdo_datum, veg_datum):
            self.kolcsonzesek.append({'kezdo_datum': kezdo_datum, 'veg_datum': veg_datum})
            return f"A(z) {self.sorszam} számú bicikli foglalva: {kezdo_datum.strftime('%Y-%m-%d')} - {veg_datum.strftime('%Y-%m-%d')}."
        else:
            return f"A(z) {self.sorszam} számú bicikli foglalt erre az időszakra."
        pass

    def kolcsonzes_datumok(self):
        kolcsonzesek_str_list = []
        for kolcsonzes in self.kolcsonzesek:
            kezdo_datum_str = kolcsonzes['kezdo_datum'].strftime('%Y-%m-%d')
            veg_datum_str = kolcsonzes['veg_datum'].strftime('%Y-%m-%d')
            kolcsonzesek_str_list.append(f"{kezdo_datum_str} - {veg_datum_str}")
        return ", ".join(kolcsonzesek_str_list)

    @abstractmethod
    def __str__(self):
        pass

class OrszagutiBiciki(Bicikli):
    def __str__(self):
        kolcsonzesek_str = self.kolcsonzes_datumok()
        return f"Típus: országúti bicikli, sorszáma: {self.sorszam}, Ár: {self.ar}, Foglalások: {kolcsonzesek_str if kolcsonzesek_str else 'Nincsenek foglalások.'}"

class HegyiBicikli(Bicikli):
    def __str__(self):
        kolcsonzesek_str = self.kolcsonzes_datumok()
        return f"Típus: hegyi bicikli, sorszáma: {self.sorszam}, Ár: {self.ar}, Foglalások: {kolcsonzesek_str if kolcsonzesek_str else 'Nincsenek foglalások.'}"

class Kolcsonzo:
    def __init__(self):
        self.biciklik = []

    def bicikli_hozzaadas(self, bicikli: Bicikli):
        self.biciklik.append(bicikli)

    def adatfeltoltes(self):
        self.bicikli_hozzaadas(OrszagutiBiciki(1, 10000))
        self.bicikli_hozzaadas(HegyiBicikli(2, 15000))
        self.bicikli_hozzaadas(HegyiBicikli(3, 15000))
        self.bicikli_hozzaadas(HegyiBicikli(4, 18000))

    def foglalasok_lekerdezes(self):
        return '\n'.join(str(bicikli) for bicikli in self.biciklik)

    def kolcsonzes(self, sorszam, kezdo_datum, veg_datum):
        for bicikli in self.biciklik:
            if bicikli.sorszam == sorszam:
                return bicikli.foglal(kezdo_datum, veg_datum)
        return "Ilyen számú bicikli nem kölcsönözhető."


def foglalas(kolcsonzo: Kolcsonzo):
    kolcsonzo.adatfeltoltes()

    while True:
        valaszt = input("Kérem válasszon: (foglalások, foglal, kilép): ")
        if valaszt == "foglalások":
            print(kolcsonzo.foglalasok_lekerdezes())
        elif valaszt == "foglal":
            sorszam = int(input("Adja meg a bicikli sorszámát: "))
            kezdo_datum_str = input("Adja meg a kezdő dátumot (yyyy-mm-dd): ")
            veg_datum_str = input("Adja meg a vég dátumot (yyyy-mm-dd): ")
            kezdo_datum = datetime.strptime(kezdo_datum_str, '%Y-%m-%d')
            veg_datum = datetime.strptime(veg_datum_str, '%Y-%m-%d')
            print(kolcsonzo.kolcsonzes(sorszam, kezdo_datum, veg_datum))
        elif valaszt == "kilép":
            print("Viszont látásra!")
            break
        else:
            print("Érvénytelen választás, próbálja újra.")



kolcsonzo = Kolcsonzo()
foglalas(kolcsonzo)