# Laboratorium 5b: Aproksymacja średniokwadratowa (Wielomiany trygonometryczne)

Repozytorium zawiera realizację drugiej części 5. laboratorium z przedmiotu Metody Obliczeniowe w Nauce i Technice (MOwNiT). Projekt stanowi odpowiedź na numeryczne bolączki bazy algebraicznej, skupiając się na wykorzystaniu bazy trygonometrycznej (sinusy i cosinusy) do aproksymacji funkcji falowych.

## 🎯 Cel projektu
Głównym celem ćwiczenia jest:
- Obiektowa implementacja bazy trygonometrycznej uwzględniającej transformację na zadany przedział przestrzenny ($L$).
- Analiza wpływu współczynnika nadmiarowości informacji ($R = n / (2m+1)$) na stabilność oznaczoność układu układu.
- Poszukiwanie "złotej harmonicznej" i analiza krzywej nasycenia informacją.
- Wykazanie przewagi transformat ortogonalnych nad klasycznymi wielomianami algebraicznymi.

## 📂 Struktura plików
- `main.ipynb` - notatnik Jupyter z implementacją generatora bazy trygonometrycznej, eksperymentami numerycznymi i generacją map cieplnych.
- `trybus_4b.pdf` - szczegółowe sprawozdanie analityczne przygotowane w systemie Typst.

## 🚀 Wymagania i uruchomienie
Wymagane jest środowisko Python 3.x:
```bash
pip install numpy matplotlib seaborn pandas ipykernel
```
Eksperymenty można odtworzyć uruchamiając komórki od góry do dołu w pliku `main.ipynb`.

## 🧠 Kluczowe wnioski z analizy
1. **Triumf ortogonalności:** Zastąpienie potęg $x$ ograniczonymi funkcjami trygonometrycznymi całkowicie eliminuje problem macierzy Vandermonde'a. Układ zyskuje wybitną odporność na błędy zmiennoprzecinkowe.
2. **Poszukiwanie "złotej harmonicznej":** Baza trygonometryczna pozwala precyzyjnie "wcelować" w częstotliwości ukryte w sygnale (np. dla $m \ge 6$ idealnie rekonstruuje $\cos(2x)$). Dalsze zwiększanie $m$ jest bezpieczne i wygaszane przez sam algorytm.
3. **Bezwzględny rygor informacyjny:** Warunkiem działania metody jest spełnienie progu $R \ge 1$. Niedobór punktów powoduje osobliwość układu, a krawędź interpolacyjna skutkuje silnym aliasingiem (myleniem częstotliwości).
4. **Zjawisko Gibbsa jako twardy limit:** Pomimo perfekcji wewnątrz przedziału, algorytm boryka się z łamaniem założenia o okresowości na brzegach (wywołanym członiem $0.5x^2$). Powoduje to lokalne przeregulowanie, stanowiące nieusuwalną "podłogę błędu" (error floor).

---
*Autor: Wiktor Trybus*