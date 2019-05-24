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
        else:
            print( "blad")
        return self.elementy

    def znajdz(self, x):
        pass

    def pobierz(self, x):
        pass



    def pojemnosc(self):
        pass


    def usun_powtorzenia(self,x):
        pass

    #def odwroc():
      #  pass

    def zwieksz_pojemnosc(x):
        pass

    def zmniejsz_pojemnosc(x):
        pass