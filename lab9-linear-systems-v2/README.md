# Laboratorium 9: Rozwiązywanie układów równań liniowych metodami iteracyjnymi

Projekt stanowi numeryczną oraz algorytmiczną analizę zbieżności iteracyjnej metody Jacobiego dla specyficznej klasy układów równań liniowych $Ax = b$. Repozytorium zawiera pełną implementację potoków pomiarowych, generację struktur danych oraz wizualizację kluczowych metryk wydajnościowych.

Projekt został zrealizowany w ramach laboratoriów z przedmiotu Metody Obliczeniowe w Nauce i Technice (MOwNiT).

## Sformułowanie problemu

Głównym obiektem badań jest układ równań scharakteryzowany przez macierz współczynników $A_{n \times n}$ zdefiniowaną jako:
- $a_{ii} = k$ dla elementów na głównej przekątnej,
- $a_{ij} = (-1)^j \cdot m / j$ dla $j > i$ (górny trójkąt),
- $a_{i, i-1} = m / i$ (dolna podprzekątna),
- $a_{ij} = 0$ dla pozostałych elementów ($j < i - 1$).

Wykładnicze wartości parametrów strukturalnych: $k = 8$, $m = 1.5$.
Rozwiązanie referencyjne $X_{ref}$ stanowi wektor o wyrazach losowanych ze zwracaniem ze zbioru $\{-1, 1\}$.

## Zakres eksperymentów

Projekt został podzielony na cztery niezależne eksperymenty badawcze:
1. **Analiza skalowalności ($n$):** Badanie wpływu rozmiaru układu $n \in [10, 500]$ na czas wykonania oraz liczbę iteracji dla dwóch odmiennych kryteriów stopu (przyrostowego oraz rezydualnego).
2. **Analiza dokładności ($\epsilon$):** Badanie wpływu parametru tolerancji $\epsilon \in [10^{-3}, 10^{-12}]$ na tempo zbieżności oraz końcowy błąd rzeczywisty.
3. **Analiza warunków początkowych ($x^{(0)}$):** Badanie wrażliwości algorytmu na odległość geometryczną wektora startowego od rozwiązania referencyjnego w normie maksimum.
4. **Analiza spektralna:** Wyznaczenie wartości własnych macierzy iteracji $M = -D^{-1}(L+U)$ i określenie promienia spektralnego $\rho(M)$ w celu weryfikacji teoretycznego warunku zbieżności.

## Struktura projektu

```text
├── main.ipynb     # Jupyter Notebook zawierający implementację i eksperymenty
├── output/                 # Katalog wyjściowy generowany automatycznie przez skrypt
│   ├── data/               # Wyniki numeryczne eksperymentów w formacie .csv
│   │   ├── experiment_1.csv
│   │   ├── experiment_2.csv
│   │   ├── experiment_3.csv
│   │   └── experiment_4.csv
│   └── plots/              # Wykresy i wizualizacje w formacie .png
│       ├── experiment_1_plots.png
│       ├── experiment_1_error_plot.png
│       ├── experiment_2_plots.png
│       ├── experiment_3_plots.png
│       └── experiment_4_plots.png
├── trybus_7.pdf            # Sprawozdanie na laboratoria
└── README.md               # Dokumentacja techniczna projektu

```

## Wymagania i środowisko

Obliczenia zostały zoptymalizowane pod kątem wektoryzacji operacji macierzowych za pomocą biblioteki NumPy.

* **Język programowania:** Python 3.13.3
* **Wymagane biblioteki:**
* numpy >= 1.26.0
* pandas >= 2.2.0
* matplotlib >= 3.8.0



## Instrukcja uruchomienia

1. Sklonuj repozytorium:
```bash
git clone https://github.com/Veexeq/MOwNiT.git)
```


2. Zainstaluj wymagane zależności:
```bash
pip install -r requirements.txt
```

3. Wejdź w odpowiedni folder:
```bash
cd lab9-linear-systems-v2
```

4. Otwórz plik `main.ipynb` i wykonaj kolejno wszystkie komórki obliczeniowe (Cell -> Run All). Stan generatora liczb losowych jest deterministyczny (ustawiony stały Seed), co gwarantuje pełną reprodukowalność wyników.

## Główne wnioski z analizy numerycznej

* **Stałość spektralna:** Promień spektralny macierzy iteracji wynosi stale $\rho(M) = 0.09375$ niezależnie od wymiarowości układu $n$, co jest bezpośrednim skutkiem silnej dominacji diagonalnej macierzy $A$.
* **Złożoność kryteriów stopu:** Kryterium przyrostowe wykazuje złożoność obliczeniową rzędu $\mathcal{O}(n)$, co czyni je drastycznie efektywniejszym czasowo od kryterium rezydualnego o złożoności $\mathcal{O}(n^2)$ dla dużych wymiarów macierzy.
* **Zbieżność geometryczna:** Ze względu na wartość $\rho(M) \approx 0.1$, każda pojedyncza iteracja algorytmu dostarcza dokładnie jedną kolejną poprawną cyfrę dziesiętną rozwiązania, determinując niską czułość układu na zaburzenia wektora początkowego.

## Autor

Wiktor Trybus  
Wydział Informatyki  
Data realizacji: Maj 2026