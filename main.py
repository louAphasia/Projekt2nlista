from mlist import MLista

def main():

    capacity=int(input( " Podaj początkowy rozmiar listy " ))

    lista=MLista(capacity)

    while True:
        polecenie = input("Wybierz pol (pisz, dodaj_element, znajdz, pobierz, rozmiar, pojemnosc,"
                          " usun_powtorzenia, odwroc, zwieksz_pojemnosc, zmniejsz_pojemnosc, wyjscie): ")
        if polecenie == "pisz":
            lista.pisz()

        elif polecenie == "dodaj_element":
            element=input(" Podaj wartosc elementu: ")
        elif polecenie == "znajdz":
            pass
        elif polecenie == "pobierz":
            pass
        elif polecenie == "rozmiar":
            pass
        elif polecenie == "pojemnosc":
            pass
        elif polecenie == "usun_powtorzenie":
            pass
        elif polecenie == "odwroc":
            pass
        elif polecenie == "zwieksz_pojemnosc":
            pass
        elif polecenie == "zmniejsz pojemnosc":
            pass
        elif polecenie == "wyjscie":
            break
        else:
            print("Bledna operacja ")



    lista.pisz()

    print(lista.rozmiar())








if __name__=="__main__":
    main()