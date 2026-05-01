# Laboratorium 5a: Aproksymacja średniokwadratowa (Wielomiany algebraiczne)

Repozytorium zawiera realizację pierwszej części 5. laboratorium z przedmiotu Metody Obliczeniowe w Nauce i Technice (MOwNiT). Projekt skupia się na dyskretnej aproksymacji średniokwadratowej funkcji o charakterze oscylacyjnym przy użyciu bazy wielomianów algebraicznych ($1, x, x^2, \dots$). 

## 🎯 Cel projektu
Głównym celem ćwiczenia jest:
- Implementacja algorytmu aproksymacji z wektorową budową układów równań normalnych.
- Zbadanie zjawisk skrajnych w modelowaniu: underfittingu oraz przeregulowania (overfittingu).
- Analiza wpływu stopnia wielomianu ($m$) oraz gęstości siatki węzłów pomiarowych ($n$) na stabilność numeryczną.
- Przeprowadzenie globalnej analizy błędu dopasowania (RMSE) za pomocą logarytmicznej mapy cieplnej w przestrzeni parametrów $(n, m)$.

## 📂 Struktura plików
- `main.ipynb` - notatnik Jupyter zawierający definicje bazy, algorytm rozwiązujący układy równań oraz procedury generujące zestawienia i krzywe błędów.
- `trybus_4a.pdf` - szczegółowe sprawozdanie z badań przygotowane w systemie Typst.

## 🚀 Wymagania i uruchomienie
Wymagane jest środowisko Python 3.x z podstawowymi bibliotekami do analizy danych:
```bash
pip install numpy matplotlib seaborn pandas ipykernel
```
Aby odtworzyć wyniki, uruchom plik `main.ipynb` w środowisku wspierającym notatniki (np. VS Code, JupyterLab) i wykonaj wszystkie komórki.

## 🧠 Kluczowe wnioski z analizy
1. **Koszmar macierzy Vandermonde'a:** Baza algebraiczna okazuje się wysoce niepraktyczna dla funkcji oscylacyjnych. Forsowanie wysokiego stopnia ($m$) prowadzi do ekstremalnego złego uwarunkowania macierzy układu normalnego, co skutkuje katastrofą zmiennoprzecinkową.
2. **Efekt Rungego:** Brak odpowiedniego narzutu danych przy wysokim stopniu wielomianu wyzwala gigantyczne, niefizyczne oscylacje międzywęzłowe, szczególnie na brzegach dziedziny.
3. **Iluzja rozwinięcia Taylora:** Choć dla bardzo gęstych siatek wielomian potrafi udawać szereg Taylora, rozwiązanie to jest inżyniersko bezużyteczne – minimalny szum w danych całkowicie zniszczyłby stabilność tego modelu.

---
*Autor: Wiktor Trybus*