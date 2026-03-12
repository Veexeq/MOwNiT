## Treść zadania
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

## Uruchomienie (*bash shell*)

### Obliczenia w C:

#### Kompilator GCC:
```
gcc -g main.c -o main_gcc.exe -Wall -lm
```

#### Kompilator MSVC:
Otworzyć folder z kodem źródłowym w `Developer Command Prompt for VS`, a następnie w tym środowisku uruchomić:
```
cl.exe /Zi /EHsc /Fe:main_msvc.exe main.c
```

### Analiza w Python:
Najpierw należy utworzyć wirtualne środowisko:
```
python -m venv .venv
```
Następnie je uruchomić:
```
source .venv/Scripts/activate
```
Następnie zainstalować moduły potrzebne do uruchomienia skryptów:
```
pip install -r requirements.txt
```
I w końcu uruchomić odpowiednie skrypty:
```
python analysis/plot_drawer.py
python analysis/err_plot_drawer.py
python analysis/delta_generator.py
python analysis/compiler_comparison.py
```

Należy wcześniej odtworzyć odpowiednią strukturę folderów, w razie problemów ze skryptami Python:
```
lab1/
|- output/
|- analysis/
|  |- graphs/
|  |  |- compiler_comp/
|  |  |- gcc/
|  |  |- msvc
|  |- precise_deltas/
```