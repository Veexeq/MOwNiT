# Laboratorium 8: Rozwiązywanie Układów Równań Liniowych

Projekt zawiera implementację oraz szczegółową analizę porównawczą algorytmów numerycznych służących do rozwiązywania układów równań liniowych: **Metody Eliminacji Gaussa** (z częściowym wyborem elementu podstawowego) oraz zoptymalizowanego **Algorytmu Thomasa** dla macierzy trójdiagonalnych. 

Głównym celem badań jest ocena wpływu precyzji zmiennoprzecinkowej (`float32` vs `float64`), rozmiaru i uwarunkowania macierzy na dokładność (norma maksimum błędu), czas wykonania oraz szczytowe zużycie pamięci (złożoność $O(n^3)$ vs $O(n)$).

## Struktura Repozytorium

```text
lab8-linear-systems/
├── data/               # Wygenerowane pliki .csv z danymi z eksperymentów (błędy, czas, pamięć)
├── plots/              # Wygenerowane wykresy (w skali liniowej oraz logarytmicznej)
├── util/               # Narzędzia CLI w Pythonie (np. konwertery CSV do formatu Typst)
├── .gitignore          # Konfiguracja ignorowanych plików dla systemu Git
├── main.ipynb          # Główny notatnik Jupyter z implementacją algorytmów i eksperymentami
└── trybus_6.pdf        # Finalne sprawozdanie wygenerowane w systemie Typst
```

## Główne funkcjonalności
* **Eliminacja Gaussa:** Zwektoryzowana implementacja z częściowym pivotingiem (odporna na macierze bliskie osobliwości).
* **Algorytm Thomasa:** Zoptymalizowana pamięciowo (działająca na jednowymiarowych wektorach przekątnych) metoda dla macierzy trójdiagonalnych.
* **Analiza Uwarunkowania:** Obliczanie współczynnika uwarunkowania (`cond`) dla generowanych klas macierzy.
* **Profilowanie:** Dokładne pomiary czasu wykonania (`time.perf_counter`) oraz zużycia pamięci RAM (`tracemalloc`).

## Wymagania
Do poprawnego uruchomienia środowiska wymagany jest język Python w wersji 3.10+ oraz podstawowe biblioteki do analizy danych i obliczeń numerycznych:
* `numpy`
* `pandas`
* `matplotlib`
* `jupyter`

## Uruchomienie

**1. Wykonanie eksperymentów:**
Wszystkie algorytmy oraz logika generująca dane wejściowe znajdują się w pliku `main.ipynb`. Notatnik ten bezpośrednio zapisuje wyniki w folderach `data/` oraz generuje bazowe wykresy w folderze `plots/`.

**2. Generowanie tabel do sprawozdania (Typst):**
W katalogu `util/` znajdują się skrypty automatyzujące tworzenie tabel w formacie Typst z plików CSV. Obsługują one argumenty wiersza poleceń (CLI). Przykład wywołania:
```bash
python util/typst_resource_formatter.py --input data/exercise3_data.csv --output util/tabela_zasobow.txt --type both
```