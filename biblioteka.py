class Knyga:
    pasiekiama = "Pasiekiama"

    def __init__(self, knygosPavadinimas, autorius, metai):
        self.knygosPavadinimas = knygosPavadinimas
        self.autorius = autorius
        self.metai = metai

    def kopijuot(self):
        return Knyga(self.knygosPavadinimas, self.autorius, self.metai)

    def pasiskolint(self):
        self.pasiekiama = "Uzimta"

    def grazinti(self):
        self.pasiekiama = "Pasiekiama"

    def rodyk(self):
        return f"{self.knygosPavadinimas} {self.autorius} {self.metai} {self.pasiekiama}"


class Biblioteka:
    def __init__(self):
        self.knygos = []

    def sukurkKopija(self, knyga):
        self.knygos.append(knyga)
        self.knygos = sorted(self.knygos, key=lambda x: (x.knygosPavadinimas, x.autorius, -x.metai))

    def get(self):
        return self.knygos

    def rodyk(self):
        # This is one possible example how you can print all books
        sarasas = []
        for knyga in self.knygos:
            sarasas.append(knyga.rodyk())
        return sarasas

    def paieska(self, pavadinimas):
        sarasas = []
        for knyga in self.knygos:
            if knyga.knygosPavadinimas == pavadinimas or knyga.autorius == pavadinimas:
                sarasas.append(knyga.rodyk())
        if sarasas:
            return sarasas
        else:
            return "--------sarasas tuscias--------"
