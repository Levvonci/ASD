# Ordine di crescita
Per $n \rightarrow \infty$ la crescita é:
$$
\boxed{1<log(n)<\sqrt n<n^a<n^{k} log^{m}(n) < c^n<n!}
$$

## Esempi di funzioni in algoritmi
### 1. Costante
- Esempio: accesso diretto a un elemento di un array
- Crescita: nulla, é indipendente da $n$

### 2. Logaritmo $log(n)$
- Crescita lenta
- Esempio: ricerca binaria $O(log(n))$

### 3. Polinomi $n^{k}$
- La base del confronto: maggiore é $k$, piú la velocitá cresce
- Esempio: algoritmi di ordinamento come il bubblesort $O(n^{2})$

### 4. Funzioni polinomiali moltiplicate per logaritmo $n^{k} log^{m}(n)$
- Crescono piú velocemente del singolo polinomio
- Esempio: algoritmi di ordinamento efficienti come il merge sort $O(nlog(n))$

### 5. Esponenziale $c^{n}$
- Cresce piú velocemente di qualsiasi altro polinomio
- Esempio: algoritmi di backtracking, come il problema del commesso viaggiatore $O(2^{n})$

### 6. Fattoriale $n!$
- Cresce piú velocemente di qualsiasi altro esponenziale
- Esempio: algoritmi che generano tutte le permutazioni di $n$ elementi

## Esempi di composizioni
Comporre funzioni le fa crescere piú velocemente:
- $log(log(n))$ cresce piú lentamente di $log(n)$
- $log(n^{k})$ = $k log(n)$ 
- $k^{n}$ cresce piú velocemente di qualsiasi $n^{k}$   

# Riepilogo

| Funzione  | Crescita            |
| --------- | ------------------- |
| Costante  | più lenta           |
| log(n)    | molto lenta         |
| √n        | tra log e n         |
| n         | lineare             |
| n log n   | poco più di lineare |
| n^2, n^3… | polinomiale         |
| c^n       | esponenziale        |
| n!        | super-esponenziale  |