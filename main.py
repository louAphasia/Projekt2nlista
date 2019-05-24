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
            element=input(" Podaj wartosc elementu: ")
            lista.dodaj_element(element)


        elif polecenie == "znajdz":
            pass
        elif polecenie == "pobierz":
            pass
        elif polecenie == "rozmiar":
            lista.rozmiar()
        elif polecenie == "pojemnosc":
            pass
        elif polecenie == "usun":
            pass
        elif polecenie == "odwroc":
            pass
        elif polecenie == "zwieksz":
            pass
        elif polecenie == "zmniejsz":
            pass
        elif polecenie == "wyjscie":
            break
        else:
            print("Bledne polecenie ")





    print(lista.rozmiar())








if __name__=="__main__":
    main()