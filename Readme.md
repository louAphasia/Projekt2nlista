# PROJEKT 2

Klasa o nazwie 'MLista' posiada następujące metody:
 * konstruktor(self, capacity) z parametrem określającym pojemność listy (liczbę elementów jaką maksymalnie może przechować),
 * pisz(self), która wypisuje informacje o liście, w tym jej aktualny rozmiar, pojemność oraz przechowywane elementy;
   Elementy listy wypisujemy tak:
dla pustej listy: Elementy: []
dla listy z czterema elementami: Elementy: [2, 1, 6, 78]
 * dodaj_element(self, x), która dodaje element x do listy pod warunkiem, że nie zostanie przekroczona jej pojemność; gdy element zostanie dodany funkcja powinna zwrócić True, w przeciwnym wypadku False
 * znajdz(self, x), której jedynym parametrem powinien być szukany element, natomiast wynikiem pozycja danego elementu w liście (licząc od 0) lub -1, gdy liczby nie ma na liście
 * pobierz(self, x) zwracającą element listy o indeksie x
 * rozmiar(self) zwracającą aktualną liczbę elementów,
 * pojemnosc(self) zwracającą aktualną pojemność listy,
 * usun_powtorzenia(self, x), która usuwa wszystkie powtórzenia danego elementu na liście, tzn. po jej wykonaniu na liście powinien być tylko pierwszy w kolejności element x


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
### Prerequisites

What things you need to install the software and how to install them

```
pip pycodestyle
```

### Installing

A step by step series of examples that tell you how to get a development env running





## Running the tests


```
python -m unittest discover
```



## Versioning

We use Python 3.7

## Authors

* **Ula Lukierska WSB II rok Informatyki * 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

