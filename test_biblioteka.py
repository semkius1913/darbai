import unittest
import biblioteka


class TestbiBlioteka(unittest.TestCase):

    def test_knyga(self):
        k1 = biblioteka.Knyga("Alain Mabanckou", "Broken Glass", 2009)
        k2 = biblioteka.Knyga("Alain Mabanckou", "Broken Glass", 2005)
        k2.pasiskolint()
        self.assertEqual(k1.rodyk(), 'Alain Mabanckou Broken Glass 2009 Pasiekiama')
        self.assertEqual(k2.rodyk(), 'Alain Mabanckou Broken Glass 2005 Uzimta')

    def test_bibliotekarodyk(self):
        b1 = biblioteka.Biblioteka()
        self.assertEqual(b1.rodyk(), [])
        b1.sukurkKopija(biblioteka.Knyga("Alain Mabanckou", "Broken Glass", 2009))
        b1.sukurkKopija(biblioteka.Knyga("Alain Mabanckou", "Broken Glass", 2005))
        b1.sukurkKopija(biblioteka.Knyga("Stieg Larsson", "The Girl With the Dragon Tattoo", 2005))
        b1.sukurkKopija(biblioteka.Knyga("Stieg Larsson", "The Girl With the Dragon Tattoo", 2008))
        b1.knygos[0].pasiskolint()
        b1.knygos[3].pasiskolint()
        b1.knygos[2].pasiskolint()
        self.assertEqual(b1.rodyk(), ['Alain Mabanckou Broken Glass 2009 Uzimta',
                                      'Alain Mabanckou Broken Glass 2005 Pasiekiama',
                                      'Stieg Larsson The Girl With the Dragon Tattoo 2008 Uzimta',
                                      'Stieg Larsson The Girl With the Dragon Tattoo 2005 Uzimta'])

    def test_bibliotekpaieska(self):
        b1 = biblioteka.Biblioteka()
        b1.sukurkKopija(biblioteka.Knyga("Alain Mabanckou", "Broken Glass", 2009))
        b1.sukurkKopija(biblioteka.Knyga("Alain Mabanckou", "Broken Glass", 2005))
        b1.sukurkKopija(biblioteka.Knyga("Stieg Larsson", "The Girl With the Dragon Tattoo", 2005))
        b1.sukurkKopija(biblioteka.Knyga("Stieg Larsson", "The Girl With the Dragon Tattoo", 2008))
        b1.knygos[0].pasiskolint()
        b1.knygos[3].pasiskolint()
        b1.knygos[2].pasiskolint()
        self.assertEqual(b1.paieska("Alain Mabanckou"), ['Alain Mabanckou Broken Glass 2009 Uzimta',
                                      'Alain Mabanckou Broken Glass 2005 Pasiekiama'])

        self.assertEqual(b1.paieska("Alain"),"--------sarasas tuscias--------")

if __name__ == '__main':
    unittest.main()
