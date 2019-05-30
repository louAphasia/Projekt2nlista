import unittest
from mlist import MLista, InvalidCapacity


class Test(unittest.TestCase):

    def test_construct_object_Capacity_Dodatnie(self):
        lista = MLista(20)
        self.assertEqual(lista.capacity, 20)

    def test_construct_object_Capacity_Zero(self):
        lista = MLista(0)
        self.assertEqual(lista.capacity, 0)

    def test_construct_object_Capacity_Negative(self):
        with self.assertRaises(InvalidCapacity):
            lista = MLista(-10)

    def test_dodaj_elementy_dodatnie(self):
        lista = MLista(10)
        lista.dodaj_element(2)

        self.assertEqual(lista.capacity, 10)
        self.assertListEqual(lista.elementy, [2])

    def test_pusta_lista_dodaj_elementy(self):
        lista = MLista(0)

        self.assertFalse(lista.dodaj_element(2))

    def test_dodaj_wiecej_niz_pojemnosc(self):
        lista = MLista(2)
        lista.dodaj_element(2)
        lista.dodaj_element(3)
        lista.dodaj_element(2)

        self.assertEqual(lista.capacity, 2)
        self.assertEqual(lista.elementy, [2, 3])
        self.assertFalse(lista.dodaj_element(3))

    def test_pojemnosc_basic(self):
        lista = MLista(5)

        self.assertEqual(lista.pojemnosc(), 5)
        self.assertEqual(lista.rozmiar(), 0)
        self.assertEqual(lista.capacity, 5)

    def test_rozmiar_basic(self):
        lista = MLista(10)
        lista.dodaj_element(2)
        lista.dodaj_element(3)
        lista.dodaj_element(4)

        self.assertEqual(lista.rozmiar(), 3)

    def test_zwieksz_pojemnosc_dodatnia_ujemne(self):
        lista = MLista(5)
        lista.zwieksz_pojemnosc(4)

        self.assertEqual(lista.capacity, 9)

        lista.zwieksz_pojemnosc(-6)

        self.assertFalse(lista.zwieksz_pojemnosc(-10))

    def test_zmniejsz_pojemnosc_basic(self):

        lista = MLista(10)
        lista.zmniejsz_pojemnosc(8)

        self.assertEqual(lista.capacity, 2)

    def test_usun_powtorzenia(self):
        lista = MLista(10)

        lista.dodaj_element(3)
        lista.dodaj_element(33)
        lista.dodaj_element(33)

        self.assertListEqual(lista.usun_powtorzenia(33), [3, 33])

    def test_odwroc(self):
        lista = MLista(4)

        lista.dodaj_element(3)
        lista.dodaj_element(111)
        lista.dodaj_element(200)
        lista.odwroc()

        self.assertListEqual(lista.elementy, [200, 111, 3])
