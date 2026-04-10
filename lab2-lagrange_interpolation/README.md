# Laboratorium 2: Interpolacja wielomianowa (Zagadnienie Lagrange'a) 📈

Repozytorium zawiera realizację 2. laboratorium z przedmiotu Metody Obliczeniowe w Nauce i Technice (MOwNiT). Projekt skupia się na implementacji i numerycznej analizie zjawiska interpolacji wielomianowej w klasycznym zagadnieniu Lagrange'a.

## 🎯 Cel projektu
Głównym celem ćwiczenia jest:
- Implementacja algorytmów interpolacji wykorzystujących postać Lagrange'a oraz wzór Newtona (ilorazy różnicowe).
- Zbadanie wpływu liczby i rozkładu węzłów (równomierne vs Czebyszewa) na dokładność przybliżenia.
- Obserwacja zjawisk numerycznych: narastania błędu interpolacji (efekt Runge'ego) oraz wpływu precyzji zmiennoprzecinkowej `float64` na stabilność algorytmów.

## 📂 Struktura plików
- `main.py` - główny punkt wejścia do aplikacji.
- `interpolators.py` - rdzeń matematyczny; zawiera generatory domknięć wyliczające wielomiany Lagrange'a i Newtona w sposób zoptymalizowany.
- `tests.py` - potoki testowe (generowanie siatek, ewaluacja, zapis błędów do CSV).
- `utils.py` - narzędzia pomocnicze: generatory węzłów oraz funkcja referencyjna $f(x)$.
- `visualizer.py` - moduł do wizualizacji wyników i błędów (Matplotlib).
- `data/` - katalog wyjściowy dla raportów z błędami w formacie `.csv`.
- `plots/` - wygenerowane wykresy interpolacji i błędów.

## 🚀 Wymagania i uruchomienie

### Zależności
Laboratoria współdzielą globalny plik `requirements.txt` znajdujący się w głównym (korzeniowym) katalogu repozytorium. Aby zainstalować wymagane pakiety, przejdź do głównego folderu projektu i wykonaj (po uprzednim aktywowaniu wirtualnego środowiska):
```bash
python -m pip install -r requirements.txt
```

### Uruchomienie eksperymentu
Aby przeprowadzić pełen zestaw testów i wygenerować wykresy dla różnych zestawów węzłów, przejdź do folderu z laboratorium i uruchom skrypt:
```bash
python main.py
```

## 🧠 Kluczowe wnioski
1. **Efekt Runge'ego:** Dla równomiernego rozkładu węzłów, błąd na brzegach przedziału drastycznie rośnie. Problem ten jest całkowicie eliminowany analitycznie poprzez zastosowanie węzłów Czebyszewa.
2. **Stabilność numeryczna (Lagrange vs Newton):** Mimo analitycznej równoważności obu wzorów, postać Newtona załamuje się przy $N \approx 60$ z powodu tzw. anihilacji cyfr znaczących (*catastrophic cancellation*) przy wyliczaniu ilorazów różnicowych. Wzór Lagrange'a jest znacznie bardziej odporny na błędy arytmetyki maszynowej.

---
*Autor: Wiktor Trybus*