# Laboratorium 3: Interpolacja wielomianowa (Zagadnienie Hermite'a) 🚀

Repozytorium zawiera realizację 3. laboratorium z przedmiotu Metody Obliczeniowe w Nauce i Technice (MOwNiT). Projekt stanowi rozwinięcie badań z Laboratorium 2, wprowadzając zagadnienie Hermite'a i zestawiając je z klasyczną interpolacją Lagrange'a.

## 🎯 Cel projektu
Głównym celem ćwiczenia jest:
- Implementacja interpolacji Hermite'a z wykorzystaniem uogólnionej metody ilorazów różnicowych ze zdublowanymi węzłami.
- Integracja analitycznej pochodnej badanej funkcji w celu "usztywnienia" wielomianu.
- Skontrastowanie zbieżności oraz limitów arytmetycznych zagadnienia Hermite'a względem zagadnienia Lagrange'a.

## 📂 Struktura plików
- `main.py` - uruchomienie potoków testowych dla interpolacji Hermite'a.
- `interpolators.py` - algorytmy numeryczne, wzbogacone o zoptymalizowaną funkcję `hermite_formula` (algorytm *in-place*).
- `tests.py` - skrypty testowe pobierające i wstrzykujące pochodną funkcji.
- `utils.py` - definicja funkcji $f(x)$ oraz jej analitycznej pochodnej $f'(x)$.
- `visualizer.py` - generowanie i zapis wykresów porównawczych na skali logarytmicznej.
- `data/` i `plots/` - zrzucone wyniki testów z podziałem na zagadnienia.

## 🚀 Wymagania i uruchomienie

### Zależności
Zależności dla wszystkich laboratoriów zarządzane są globalnie. Upewnij się, że zainstalowałeś pakiety z pliku `requirements.txt` znajdującego się w głównym katalogu repozytorium (po uprzednim aktywowaniu wirtualnego środowiska):
```bash
# Z poziomu głównego katalogu repozytorium:
pip install -r requirements.txt
```

### Uruchomienie eksperymentu
Będąc w katalogu trzeciego laboratorium, uruchom proces generowania wykresów i analizy błędów poleceniem:
```bash
python main.py
```

## 🧠 Kluczowe wnioski z analizy (Hermite vs Lagrange)
1. **Problem niedopróbkowania (Undersampling):** Dla małej liczby węzłów (np. $N=10$) zagadnienie Hermite'a generuje potężne oscylacje, które łudząco przypominają efekt Runge'ego, ale w rzeczywistości wynikają ze zbyt małej gęstości próbkowania dla funkcji oscylującej ($cos(2x)$).
2. **"Złoty środek" (Sweet Spot):** Dla $N=20$ zagadnienie Hermite'a deklasuje Lagrange'a, niemal idealnie pokrywając się z funkcją oryginalną dzięki narzuceniu warunków na pierwszą pochodną.
3. **Pułapka stopnia wielomianu:** Ponieważ dla $N$ węzłów wielomian Hermite'a osiąga stopień $2N-1$, arytmetyka zmiennoprzecinkowa (`float64`) załamuje się tu dwukrotnie szybciej. Całkowita destrukcja numeryczna następuje już dla $N \approx 30$ (co odpowiada momentowi awarii postaci Newtona dla $N \approx 60$ z Lab 2). 

---
*Autor: Wiktor Trybus*