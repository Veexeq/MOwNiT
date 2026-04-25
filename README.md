# MOwNiT: Metody Obliczeniowe w Nauce i Technice 🧮

Kolekcja projektów, algorytmów i skryptów analitycznych realizowanych w ramach laboratorium z przedmiotu **Metody Obliczeniowe w Nauce i Technice** na kierunku **Informatyka** na **Wydziale Informatyki Akademii Górniczo-Hutniczej im. Stanisława Staszica w Krakowie (AGH)** w roku akademickim 2025/2026.

> **Status projektu:** 🚧 Work in Progress  
Repozytorium jest aktywnie rozwijane i będzie systematycznie uzupełniane o kolejne zagadnienia wraz z postępem semestru.

## 📂 Struktura repozytorium

Poniżej znajduje się lista zrealizowanych do tej pory laboratoriów. Kliknij w nazwę folderu, aby przejść do szczegółowej dokumentacji i instrukcji uruchomienia danego zadania.

* **[Lab 1: Arytmetyka Komputerowa](./lab1)** - Badanie własności arytmetyki zmiennoprzecinkowej, analiza błędów zaokrągleń oraz zjawiska utraty cyfr znaczących na przykładzie ciągów nieliniowych. Obliczenia w C, analiza i wizualizacja w Pythonie.
* **[Lab 2: Interpolacja Lagrange'a](./lab2-lagrange_interpolation)** - Implementacja algorytmów interpolacji wielomianowej za pomocą wzorów Lagrange'a i Newtona. Porównanie węzłów równoodległych z węzłami Czebyszewa oraz analiza zjawiska Rungego. Zrealizowane w Pythonie (`numpy`, `matplotlib`).
* **[Lab 3: Interpolacja Hermite'a](./lab3-hermite_interpolation)** - Wykorzystanie wielomianów Hermite'a do interpolacji danych uwzględniających nie tylko wartości funkcji, ale również jej pochodne w węzłach. Implementacja algorytmu różnic dzielonych i analiza wizualna przybliżenia.
* **[Lab 4: Interpolacja funkcjami sklejanymi](./lab4-spline)** - Implementacja interpolacji funkcji przy użyciu splajnów kwadratowych oraz sześciennych. Porównanie wpływy warunków brzegowych, w tym warunku *clamped* i naturalnego.
* **[Lab 5: Aproksymacja wielomianami algebraicznymi](./lab5-polynomial-approx)** - Aproksymowanie funkcji referencyjnej operując nieortogonalną bazą składającą się z wielomianów algebraicznych, porównanie dokładności w zależności od liczby punktów referencyjnych oraz stopnia bazy.
* **Lab 6+:** *Kolejne tematy wkrótce...*

## 🚀 Jak korzystać z projektów?

Każde laboratorium stanowi oddzielny, zorganizowany projekt. Ze względu na zróżnicowanie technologii (C, Python), **szczegółowe instrukcje kompilacji oraz tworzenia środowisk wirtualnych (`venv`) znajdują się wewnątrz poszczególnych folderów w plikach `README.md`.**

### Ogólne wymagania
Aby mieć pewność, że wszystkie programy i skrypty w tym repozytorium uruchomią się poprawnie, Twój system powinien posiadać:
* **Interpreter Pythona 3.8+** (wraz z menedżerem pakietów `pip`).
* **Kompilator języka C** (np. GCC przez MSYS2/MinGW lub MSVC).
* Opcjonalnie: Git do klonowania repozytorium.

## 👤 Autor
**Wiktor Trybus**