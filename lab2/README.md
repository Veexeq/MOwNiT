# Interpolacja Numeryczna: Lagrange i Newton

Projekt zrealizowany w ramach laboratorium 2 z Metod Obliczeniowych w Nauce i Technice. Program w języku Python służący do wyznaczania wielomianów interpolujących (Lagrange'a i Newtona) oraz wizualizacji wyników.

## Funkcjonalności

* **Wzory interpolacyjne:** Wyznaczanie wielomianu przy użyciu metody Lagrange'a oraz Newtona.
* **Rozmieszczenie węzłów:**
  * Równomierne w całym zadanym przedziale (uwzględniając końce).
  * Zgodnie z zerami wielomianu Czebyszewa (minimalizacja błędu interpolacji na brzegach przedziału).
* **Wizualizacja:** Rysowanie wykresów funkcji na podstawie:
  * Zadanej, określonej liczby punktów.
  * Zadanego wzoru analitycznego (porównanie funkcji oryginalnej z wielomianem interpolującym).

## Wymagania

Do uruchomienia projektu wymagany jest interpreter języka Python (wersja 3.8 lub nowsza) oraz następujące biblioteki:

* `numpy` - do operacji na macierzach i wektorach.
* `matplotlib` - do generowania wykresów.

> **Wskazówka:** Zaleca się uruchamianie projektu w wirtualnym środowisku (np. `venv` lub `conda`).

## Instalacja

1. Sklonuj repozytorium na swój dysk lokalny:
```bash
git clone https://github.com/Veexeq/MOwNiT
cd lab2
```

2. Utwórz i aktywuj środowisko wirtualne (opcjonalnie, ale zalecane):
```bash
python -m venv .venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

3. Zainstaluj wymagane pakiety:
```bash
pip install -r requirements.txt
```

## Użycie

Aby uruchomić program i wygenerować przykładowe wykresy, wykonaj główny skrypt z poziomu terminala:

```bash
python main.py
```

## Struktura plików projektu

* `main.py` - Główny skrypt uruchamiający program i opcje wizualizacji.
* `interpolators.py` - Implementacja algorytmów Lagrange'a i Newtona.
* `utils.py` - Funkcje pomocnicze, w tym generowanie węzłów równoodległych i Czebyszewa.
* `requirements.txt` - Lista zależności Pythona.