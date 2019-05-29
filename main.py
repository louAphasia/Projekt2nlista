from mlist import MLista


def main():
    while True:
        try:
            capacity = int(input(" Podaj początkowy rozmiar listy "))
            lista = MLista(capacity)
            if capacity >= 0:
                break
        except ValueError:
            print('Mozna wpisac tylko Integers')
            continue

    while True:
        polecenie = input("Wybierz polecenie (pisz, dodaj_element, znajdz, pobierz, rozmiar, pojemnosc,"
                          " usun_powtorzenia, odwroc, zwieksz_pojemnosc, zmniejsz_pojemnosc, wyjscie): ")
        if polecenie == "pisz":
            lista.pisz()

        elif polecenie == "dodaj_element":
            try:
                element = int(input(" Podaj wartosc elementu: "))
                print(lista.dodaj_element(element))
            except ValueError:
                print('Mozna wpisac tylko Integers')



        elif polecenie == "znajdz":
            try:
                element = int(input("Podaj którego elementu indeks chcesz znaleźć "))
                print(lista.znajdz(element))
            except ValueError:
                print('Mozna wpisac tylko Integers')

        elif polecenie == "pobierz":
            try:
                index = int(input(" Podaj indeks którego element chcesz pobirac "))
                print(lista.pobierz(index))
            except ValueError:
                print('Mozna wpisac tylko Integers')

        elif polecenie == "rozmiar":
            print(lista.rozmiar())

        elif polecenie == "pojemnosc":
            print(lista.pojemnosc())

        elif polecenie == "usun_powtorzenia":
            try:
                element = int(input(" Podaj którego elementu powtorzenia maja byc usuniete "))
                lista.usun_powtorzenia(element)
            except ValueError:
                print('Mozna wpisac tylko Integers')

        elif polecenie == "odwroc":
            lista.odwroc()

        elif polecenie == "zwieksz_pojemnosc":
            try:
                x = int(input( "Podaj wartosc "))
                print(lista.zwieksz_pojemnosc(x))
            except ValueError:
                print('Mozna wpisac tylko Integers')

        elif polecenie == "zmniejsz_pojemnosc":
            try:
                x = int(input("Podaj wartosc "))
                print(lista.zmniejsz_pojemnosc(x))
            except ValueError:
                print('Mozna wpisac tylko Integers')

        elif polecenie == "wyjscie":
            break
        else:
            print("Bledne polecenie ")


if __name__ == "__main__":
    main()
