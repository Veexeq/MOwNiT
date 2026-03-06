### Treść zadania
***
#### Wyznaczyć kolejne elementy ciągu:
$$
\begin{gather*}
    x_{k+1} = 
    \begin{cases}
        x_k + 3x_k \cdot (1 - x_k) \quad &k \geq 1 \\
        x_k = 0.1 \quad &k = 1
    \end{cases}
\end{gather*}
$$
Porównać otrzymane wartości dla różnej precyzji zmiennych: `float`, `double`, `long double`.  

#### Następnie użyć przekształconej postaci wzoru:
$$
\begin{gather*}
    x_{k+1} = 
    \begin{cases}
        4x_k - 3x_k x_k \quad &k \geq 1 \\
        x_k = 0.1 \quad &k = 1
    \end{cases}
\end{gather*}
$$
Spróbować wyjaśnić otrzymane wyniki.  

#### Powtórzyć obliczenia dla:
1. $x_0 = 0.1000001$
2. $x_0 = 0.1000000000000001$

Porównać rozwój błędu dla różnych precyzji zmiennych.