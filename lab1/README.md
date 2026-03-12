# Lab 1: Arytmetyka Komputerowa

## 🎓 Treść zadania nr 6:
#### Wyznaczyć kolejne elementy ciągu:
$$
x_{k+1} = \begin{cases} 
x_k + 3x_k(1 - x_k) & k \geq 1 \\ 
x_k = 0.1 & k = 1 
\end{cases}
$$

#### Następnie użyć przekształconej postaci wzoru:
$$
x_{k+1} = \begin{cases} 
4x_k - 3x_k^2 & k \geq 1 \\ 
x_k = 0.1 & k = 1 
\end{cases}
$$

Spróbować wyjaśnić otrzymane wyniki.  

#### Powtórzyć obliczenia dla:
1. $x_0 = 0.1000001$
2. $x_0 = 0.1000000000000001$

Porównać rozwój błędu dla różnych precyzji zmiennych.

***

## 🛠️ Część 1: Kompilacja i uruchamianie (C)

### Wymagania wstępne
* **GCC:** (np. poprzez MSYS2 lub MinGW) dodane do zmiennej środowiskowej `PATH`.
* **MSVC:** Narzędzia Build Tools for Visual Studio 2022 (lub nowsze).

### Ręczna kompilacja z poziomu terminala
Przejdź w terminalu do folderu z plikiem `main.c` i wykonaj poniższe kroki w zależności od wybranego kompilatora.

**Użycie GCC:**
```bash
mkdir build
gcc -g main.c -o build/main_gcc.exe -Wall -lm
```

**Użycie MSVC:**
Otwórz specjalny terminal **Developer Command Prompt for VS**, utwórz folder `build` i wywołaj kompilator:
```cmd
mkdir build
cl.exe /Zi /EHsc /Fo"build\\" /Fd"build\\" /Fe:"build\main_msvc.exe" main.c
```

---

## 🐍 Część 2: Analiza danych (Python)

Zestaw skryptów w języku Python służy do wizualizacji danych wygenerowanych przez programy w C oraz generacji ciągu referencyjnego (ciąg z dokładnością do stu liczb po przecinku).

### 1. Przygotowanie środowiska wirtualnego
Zalecane jest uruchamianie skryptów w izolowanym środowisku wirtualnym, aby uniknąć konfliktów wersji bibliotek. W głównym katalogu projektu utwórz środowisko o nazwie `.venv`:

```bash
python -m venv .venv
```

Następnie aktywuj środowisko. Komenda zależy od Twojego systemu operacyjnego i używanego terminala:
* **Windows (Git Bash):** `source .venv/Scripts/activate`
* **Windows (CMD):** `.venv\Scripts\activate.bat`
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
* **Linux / macOS:** `source .venv/bin/activate`

Po poprawnej aktywacji w terminalu przed znakiem zachęty pojawi się przedrostek `(.venv)`.

### 2. Instalacja zależności
Mając aktywne środowisko wirtualne, zainstaluj wszystkie wymagane pakiety analityczne z pliku konfiguracyjnego:

```bash
pip install -r requirements.txt
```

### 3. Wymagana struktura katalogów
Skrypty analityczne zapisują wygenerowane wykresy i dane w ściśle określonych folderach. Przed ich uruchomieniem upewnij się, że w Twoim katalogu roboczym (np. `lab1/`) istnieje poniższa struktura. Jeśli brakuje jakichś folderów, utwórz je ręcznie:

```text
lab1/
├── analysis/
│   ├── graphs/
│   │   ├── compiler_comp/
│   │   ├── gcc/
│   │   └── msvc/
│   └── precise_deltas/
└── output/
```

### 4. Uruchamianie skryptów
Gdy środowisko jest aktywne, a foldery gotowe, możesz wygenerować wyniki analizy. Wywołuj skrypty z głównego katalogu:

```bash
# Rysowanie podstawowych wykresów
python analysis/plot_drawer.py

# Rysowanie wykresów dotyczących błędów między typami
python analysis/err_plot_drawer.py

# Generowanie dokładnych delt (odchyłek od wartości referencyjnych)
python analysis/delta_generator.py

# Generowanie zestawienia porównawczego kompilatorów (GCC vs MSVC)
python analysis/compiler_comparison.py
```

Wygenerowane pliki i wykresy znajdziesz w odpowiednich podfolderach w `analysis/graphs/`.

*Aby wyjść ze środowiska wirtualnego po zakończeniu pracy, wpisz komendę:* `deactivate`

---

## 📊 Wyniki i wnioski z obserwacji

Podsumowanie przeprowadzonych testów, analiza porównawcza oraz wnioski z ćwiczenia zostały zebrane w formie czytelnej prezentacji. 

Zachęcam do zapoznania się z plikiem **[`slides.pdf`](./slides.pdf)** (znajdującym się w głównym katalogu repozytorium), który zawiera interpretację wygenerowanych danych i wykresów.

---

## 🎓 O projekcie

Projekt ten został zrealizowany na potrzeby kursu **Metody Obliczeniowe w Nauce i Technice (MOwNiT)**, realizowanego na **Akademii Górniczo-Hutniczej im. Stanisława Staszica w Krakowie (AGH)** w roku 2025/26.