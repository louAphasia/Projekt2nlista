class MLista():
    def __init__(self, capacity):
        if capacity >= 0:
            self.capacity = capacity
            self.elementy = []
        else:
            raise InvalidCapacity("prosze wpisac pojemnosc Nieujemna")

    def rozmiar(self):
        size = int()
        for x in self.elementy:
            size += 1
        return size

    def pisz(self):
        print("Rozmiar aktualny listy: ", MLista.rozmiar(self))
        print("Pojemnosc listy: ", self.capacity)
        print("Elementy: ", self.elementy)

    def dodaj_element(self, x):
        if self.capacity > len(self.elementy):
            self.elementy.append(x)
            return True
        else:
            return False

    def znajdz(self, x):
        if x in self.elementy:
            return self.elementy.index(x)
        else:
            return -1

    def pobierz(self, x):
        if x < self.capacity:
            return self.elementy[x]
        else:
            print("Nie ma takiego indeksu")

    def pojemnosc(self):
        return self.capacity

    def usun_powtorzenia(self, x):

        indices = [i for i, a in enumerate(self.elementy) if a == x]
        for x in indices[1:]:
            self.elementy[x] = 'del'
        self.elementy = [p for p in self.elementy if p != 'del']
        return self.elementy

    def odwroc(self):
        return self.elementy.reverse()

    def zwieksz_pojemnosc(self, x):
        if x >= 0:
            self.capacity = self.capacity + x
            return True
        else:
            return False

    def zmniejsz_pojemnosc(self, x):
        if self.capacity - x > (len(self.elementy) - 1):
            self.capacity = self.capacity - x
            return True
        else:
            return False


class InvalidCapacity(ValueError):
    def __init__(self, msg):
        super().__init__(msg)
