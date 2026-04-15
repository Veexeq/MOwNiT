# Laboratorium 4: Interpolacja funkcjami sklejanymi (Splajny)

Repozytorium zawiera realizację 4. laboratorium z przedmiotu Metody Obliczeniowe w Nauce i Technice (MOwNiT). Projekt skupia się na interpolacji oscylującej funkcji analitycznej za pomocą funkcji sklejanych (splajnów) 2. i 3. stopnia, ze szczególnym uwzględnieniem wpływu warunków brzegowych na stabilność numeryczną.

## 🎯 Cel projektu
Głównym celem ćwiczenia jest:
- Obiektowa implementacja splajnów kwadratowych ($C^1$) oraz sześciennych ($C^2$).
- Implementacja i analiza wpływu różnych warunków brzegowych (m.in. utwierdzony, naturalny, brak krzywizny początkowej).
- Rozwiązanie globalnego układu równań dla splajnów sześciennych za pomocą zoptymalizowanego algorytmu Thomasa dla macierzy trójprzekątniowej.
- Porównanie rzędów zbieżności i propagacji błędu (MBB, RMSE) w zależności od stopnia wielomianu i gęstości siatki.

## 📂 Struktura plików
- `main.ipynb` - główny notatnik Jupyter zawierający wyprowadzenia matematyczne, kod obiektowy, testy oraz generację wszystkich wykresów i tabel badawczych.
- `trybus_3.pdf` - sprawozdanie z badań przygotowane w systemie Typst.
- `figures/spline_n*.png` oraz `figures/spline_errors.png` - zrzucone wizualizacje wygenerowane przez notatnik.
- `errors.html` - wyeksportowana tabela ze zrzutem błędów dla różnej liczby przedziałów $N$.

## 🚀 Wymagania i uruchomienie

### Zależności
Zależności zarządzane są globalnie dla wszystkich laboratoriów. Projekt wymaga zainstalowania dodatkowych pakietów do obsługi notatników oraz analizy danych (po uprzednim aktywowaniu wirtualnego środowiska):
```bash
# Z poziomu głównego katalogu repozytorium:
pip install -r requirements.txt

# Upewnij się, że masz zainstalowane kluczowe pakiety dla tego laboratorium:
pip install numpy matplotlib pandas ipykernel
```

### Uruchomienie eksperymentu
Projekt został zrealizowany w formie interaktywnego notatnika. 
1. Otwórz plik `main.ipynb` w środowisku wspierającym notatniki (np. Visual Studio Code z rozszerzeniem Jupyter lub w przeglądarkowym JupyterLab).
2. Upewnij się, że wybrano odpowiednie jądro (Kernel) połączone z Twoim środowiskiem wirtualnym `.venv`.
3. Uruchom wszystkie komórki od góry do dołu (`Run All`), aby prześledzić proces od definicji matematycznych po wizualizację tabel błędów na końcu.

## 🧠 Kluczowe wnioski z analizy (Stopień 2 vs Stopień 3)
1. **Propagacja błędu (Stopień 2):** Interpolacja splajnami kwadratowymi, a dokładniej mój sposób jej realizacji, jest silnie narażony na kumulację błędów. Wynika to z iteracyjnego sposobu wyliczania współczynników "od lewej do prawej". Najmniejsza niedokładność na początku przedziału skutkuje drastycznym rozjechaniem się krzywej na prawym krańcu (szczególnie widoczne dla $N \approx 20$).
2. **Globalna stabilność (Stopień 3):** Splajny sześcienne, dzięki rozwiązywaniu współczynników globalnie (macierz trójprzekątniowa), idealnie równoważą "naprężenia" krzywej. Deklasują one stopień kwadratowy pod kątem stabilności i wierności dla funkcji o dużej zmienności.
3. **Pułapka warunku naturalnego:** Teoretycznie domyślny warunek naturalny (zerowa druga pochodna na brzegach) drastycznie pogarsza dokładność, jeśli badana funkcja posiada na krańcach bardzo wysoką krzywiznę ($f''(3\pi) = 41$). Warunek "utwierdzony" z narzuconą pochodną analityczną sprawdza się w tym scenariuszu o kilka rzędów wielkości lepiej.
4. **Dynamika zbieżności:** Analiza wykresów log-log bezsprzecznie udowadnia znacznie wyższy rząd zbieżności ($O(h^4)$) metod trzeciego stopnia.

---
*Autor: Wiktor Trybus*