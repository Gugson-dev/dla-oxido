# Jak działa aplikacja?
Aplikacja napisana w kodzie python generuje plik atrykul.html przy użyciu sztucznej inteligencji - przesyła jej artykuł w surowej formie, a następnie za pomocą odpowiednio skomponowanego zapytania, prosi o utworzenie kodu HTML który będzie pokazywał go w ułożonej formie, a na koniec kod ten zapisuje do pliku artykul.html. Ponadto zostało wykonane zadanie dla chętnych które przy pomocy kodu HTML zawartego w plikach szablon.html i podglad.html, a także pyscriptu w tym drugim, generuje odpowiednią strone w raz z artykułem łącząc sformatowaną treść artykułu w pliku artykul.html z przygotowanym szablonem w pliku szablon.html.
# Instrukcja
## Krok 1 - Obsługa plików
Pliki pobierz i przenieś do jednego folderu
## Krok 2 - Urchomienie pliku
>[!WARNING]
>Zanim wykonasz poniższe polecenia upewnij się, że masz zainstalowanego i skonfigurowanego pythona na stanowisku.  
(Dla windows, ponieważ jest to system z którego korzystam: [Using Python on Windows](https://docs.python.org/3/using/windows.html)) 

Zainstaluj biblioteke openai -  w wierszu poleceń użyj następującej komendy:
```
pip install openai
```
Uruchom plik zadanie_oxido.py - w wierszu poleceń przejdź do katalogu w którym znajdują się pliki, a następnie użyj komendy:  
```
python zadanie_oxido.py
```
(Jeżeli w powyższym wystąpiły jakieś błędy oznacza to, że prawdopodobnie klucz API jest zły, wpisz więc na jego miejsce poprawny - 5 linia kodu między apostrofami - api_key='wpisz klucz tutaj')
## Krok 3 - Podgląd (Zadanie dla chętnych)
Uruchom lokalny serwer python - w wierszu poleceń przejdź do katalogu w którym znajdują się pliki, a następnie użyj komendy: 
```
python -m http.server
```  
Na serwerze python, otwórz plik "podglad.html" - standardowo jest to "http://localhost:8000/podglad.html"
