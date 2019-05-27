from mlist import MLista

def main():

    capacity=int(input( " Podaj początkowy rozmiar listy " ))

    lista=MLista(capacity)



    while True:
        polecenie = input("Wybierz pol (pisz, de, znajdz, pobierz, rozmiar, pojemnosc,"
                          " usun, odwroc, zwieksz, zmniejsz, wyjscie): ")
        if polecenie == "pisz":
            lista.pisz()

        elif polecenie == "de":
            element=int(input(" Podaj wartosc elementu: "))
            lista.dodaj_element(element)

        elif polecenie == "znajdz":
             element=int(input("Podaj którego elementu indeks chcesz znaleźć "))
             print(lista.znajdz(element))

        elif polecenie == "pobierz":
             index=int(input(" Podaj indeks którego element chcesz pobirac "))
             print(lista.pobierz(index))

        elif polecenie == "rozmiar":
            print(lista.rozmiar())

        elif polecenie == "pojemnosc":
            print(lista.pojemnosc())

        elif polecenie == "usun":
            element=int(input( " Podaj którego elementu powtorzenia maja byc usuniete "))
            lista.usun_powtorzenia(element)


        elif polecenie == "odwroc":
            lista.odwroc()

        elif polecenie == "zwieksz":
            x=int(input( "Podaj wartosc"))
            print(lista.zwieksz_pojemnosc(x))

        elif polecenie == "zmniejsz":
            x = int(input("Podaj wartosc"))
            print(lista.zmniejsz_pojemnosc(x))

        elif polecenie == "wyjscie":
            break
        else:
            print("Bledne polecenie ")





    print(lista.rozmiar())








if __name__=="__main__":
    main()