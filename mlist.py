class MLista(list):

    def __init__(self, capacity):
        self.capacity=capacity
        self.elementy=[]

    def rozmiar(self):
        size=int()
        for x in self.elementy:
            size+=1
        return size

    def pisz(self):
        print("Rozmiar aktualny listy:", MLista.rozmiar(self))
        print(" Pojemnosc listy : ",self.capacity)
        print("Elementy: " , self.elementy)

    def dodaj_element(self, x):
        if self.capacity>len(self.elementy):
            self.elementy.append(x)
            return True
        else:
            print( "blad")
        return False

    def znajdz(self, x):
        if x in self.elementy:
            MLista.index(x)
        else:
            -1

    def pobierz(self, x):
        if x> self.capacity:
            return self.elementy[x]



    def pojemnosc(self):
        return self.capacity


    def usun_powtorzenia(self,x):
        pass

    def odwroc(self):
        return MLista.reverse(self.elementy)



    def zwieksz_pojemnosc(self,x):
        if x>=0:
            self.capacity=self.capacity+x
            return True
        else:
            print("Wystapil blad")
            return False

    def zmniejsz_pojemnosc(self,x):
        if self.capacity-x<len(self.elementy):
            self.capacity=self.capacity-x
            return True
        else:
            print("Wystapil blad")
            return False