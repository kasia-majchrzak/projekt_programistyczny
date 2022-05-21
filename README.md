# NLP-APP 

Aplikacja webowa pozwalająca na generowanie chmury słów, tworzenie streszczeń oraz porównywanie dwóch tekstów.

## Chmury
- Możliwe wczytanie tekstu z pliku bądź wpisanie tekstu
- Generowanie chmury słów
- Możliwość pobrania chmury w postaci pliku jpg

## Streszczenie
- Możliwe wczytanie tekstu z pliku bądź wpisanie tekstu
- Generowanie streszczenia z wczytanego tekstu
- Możliwość pobrania pliku w formacie .txt, który zawiera wygenerowane streszczenie

## Porównywanie tekstów
- Możliwe wczytanie dwóch plików bądź wpisanie tekstu
- Aplikacja zwraca procent podobieństwa tekstów do siebie

## Struktura projektu
Projekt zawiera 2 foldery: folder z frontendem napisanym w Angularze oraz folder zawierający backend aplikacji napisany w pythonie (z wykorzystaniem Django)

## Frameworki, biblioteki
- Django
- Angular
- nltk
- scikit-learn
- numpy
- pandas

## Uruchomienie aplikacji
Aby uruchomić aplikację lokalnie, należy przejść do folderu, który zawiera frontend aplikacji oraz uruchomić konsolę cmd.
Następnie w konsoli należy wpisać polecenie `ng serve`

Aby uruchomić backend aplikacji należy przejść do folderu, który zawiera backend oraz uruchomić konsolę cmd. 
Następnie w konsoli należy wpisać polecenie `python manage.py runserver`

## Dokumentacja swaggerowa
Jeżeli uruchomimy aplikację lokalnie, dokumentacja znajduje się pod adresem `http://127.0.0.1:8000/docs/`