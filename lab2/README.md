# Interpolacja Numeryczna: Lagrange, Newton i Hermite

Projekt zrealizowany w ramach laboratorium z Metod Obliczeniowych w Nauce i Technice (MOwNiT). Program w języku Python służący do wyznaczania wielomianów interpolujących różnymi metodami, wizualizacji zjawiska Rungego oraz zaawansowanej analizy błędów numerycznych.

## Funkcjonalności

* **Wzory interpolacyjne:** 
  * Metoda Lagrange'a.
  * Metoda Newtona (zoptymalizowana z użyciem ilorazów różnicowych).
  * Metoda Hermite'a (wykorzystująca wartości funkcji oraz jej analitycznie wyliczonej pierwszej pochodnej).
* **Rozmieszczenie węzłów:**
  * Równomierne w zadanym przedziale.
  * Zgodne z pierwiastkami wielomianu Czebyszewa (w celu minimalizacji zjawiska Rungego na brzegach przedziału).
* **Analiza błędów:**
  * Obliczanie błędu maksymalnego oraz zadanego błędu średniego.
  * Zapisywanie szczegółowych logów z wynikami testów do plików `.csv`.
* **Wizualizacja:** 
  * Generowanie wykresów porównujących funkcję analityczną z wielomianem interpolującym.
  * Generowanie zbiorczych wykresów błędów w skali logarytmicznej w zależności od liczby węzłów (N).

## Wymagania

Do uruchomienia projektu wymagany jest interpreter języka Python (wersja 3.8 lub nowsza) oraz następujące biblioteki:

* `numpy` - do operacji na macierzach, wektorach i szybkiej ewaluacji wielomianów (schemat Hornera).
* `matplotlib` - do generowania wykresów.  
  
> **Wskazówka:** Zaleca się uruchamianie projektu w wirtualnym środowisku (np. `venv` lub `conda`).

## Instalacja

1. Sklonuj repozytorium na swój dysk lokalny:
```bash
git clone [https://github.com/Veexeq/MOwNiT](https://github.com/Veexeq/MOwNiT)
cd lab2
```

2. Utwórz i aktywuj środowisko wirtualne (opcjonalnie, ale zalecane):
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

3. Zainstaluj wymagane pakiety (jeśli posiadasz plik requirements.txt):
```bash
pip install -r requirements.txt
```
*(Alternatywnie: `pip install numpy matplotlib`)*

## Użycie

Aby uruchomić program, wygenerować raporty błędów i zapisać wykresy, wykonaj główny skrypt z poziomu terminala:

```bash
python main.py
```

Po zakończeniu działania programu, wyniki znajdziesz w nowo utworzonych folderach:
* Folder `plots/` – zawiera wygenerowane wykresy podzielone na podkatalogi dla poszczególnych metod (np. `lagrange`, `hermite`).
* Folder `data/` – zawiera pliki `.csv` z wynikami analizy błędów.

## Struktura plików projektu

* `main.py` - Główny skrypt sterujący wykonaniem programu.
* `interpolators.py` - Implementacja algorytmów obliczających wielomiany (Lagrange, Newton, Hermite).
* `utils.py` - Funkcje pomocnicze, generatory węzłów, funkcje testowe (np. funkcja Rungego) oraz ich analityczne pochodne.
* `tests.py` - Logika testująca. Definiuje procedury do masowego testowania różnych liczebności węzłów i generuje pliki CSV z wynikami.
* `visualizer.py` - Moduł odpowiedzialny za renderowanie, formatowanie i zapisywanie wykresów na dysku.