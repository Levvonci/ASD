# Algoritmo di Kruskal
L'algoritmo di Kruskal serve per trovare il **Minimum Spannin Tree (MST)**, ovvero un insieme di archi che:
- Collega tutti i vertici del grafo
- Non contiene cicli
- Costo totale minimo
## Idea di base
Kruskal parte da tutti i vertici isolati (ognuno di essi é un piccolo albero) e **aggiunge gli archi piú economici** uno alla volta, purché non si creino cicli.
È un approccio *Bottom-Up*:
parte da una foresta di alberi singoli e li unisce gradualmente.	

>[!pensiero]
>Prendo l'arco piú economico possibile che collega due componenti distinte

## Algoritmo Step-By-Step
Supponiamo di avere un grafo con pesi reali $c_{e}$

### Passo_1: Ordina tutti gli archi per costo crescente
```Pseudo
Archi (peso):
(A,B,1), (A,C,2), (B,C,3), (C,D,5), ...
```

### Passo_2: Inizializza una foresta
Ogni vertice é un albero separato
```Pseudo
A   B   C   D
```

### Passo_3: Scorri gli archi in ordine crescente
Per ogni arco $(u,v)$:
- Se l'arco collega due insiemi distinti $\rightarrow$ aggiungilo ad MST;
- Se l'arco collega due vertici giá connessi $\rightarrow$ scartalo (formerebbe un ciclo)

### Passo_4: Termina quando hai $n-1$ archi
Dove $n$ é il numero dei vertici

### Esempio:
```Pseudo
  (A)--1--(B)
   | \     |
   4  2    3
   |    \  |
  (D)--5--(C)
```

| Arco  | Peso | Azione                 | MST Risultante      |
| ----- | ---- | ---------------------- | ------------------- |
| (A,B) | 1    | Aggiunto               | {(A,B)}             |
| (A,C) | 2    | Aggiunto               | {(A,B),(A,C)}       |
| (B,C) | 3    | Scartato (Forma Ciclo) | {(A,B),(A,C)}       |
| (A,D) | 4    | Aggiunto               | {(A,B),(A,C),(A,D)} |
| (C,D) | 5    | Scartato (Forma Ciclo) | {(A,B),(A,C),(A,D)} |
\# Vertici = 4, \# Archi = 3
$n = 4$, $n-1$ Archi
Costo Totale = 1+2+4 = 7

## Come faccio a sapere se un arco crea un ciclo?
Durante l'esecuzione di Kruskal bisogna continuamente sapere se:
- Due vertici appartengono allo stesso albero (Quindi giá connessi)
- Due vertici appartengono ad insiemi diversi (Quindi si possono unire senza creare vertici)
Utilizziamo la **Union-Find** per gestire insiemi disgiunti dinamici in tempo quasi constante

## Pseudo-Codice
```Pseudo
Kruskal(G):
    T = ∅
    Ordina gli archi per peso crescente
    Per ogni vertice v:
        makeSet(v)
    Per ogni arco (u, v) in ordine:
        if find(u) ≠ find(v):
            add (u, v) a T
            union(u, v)
    return T
```

*Operazioni della **Union-Find***:
1. `makeSet(x)` $\rightarrow$ crea un insieme contenente solo `x` (All'inizio ogni vertice é separato)
2. `find(x)` $\rightarrow$ resituisce il rappresentate dell'insieme `x` (La radice)
3. `union(A,B)` $\rightarrow$ unisce i due insiemi contenenti `A` e `B`, con `A` radice

### Complessitá dell'Algoritmo

| Operazione                         | Costo                          |
| ---------------------------------- | ------------------------------ |
| Ordinare gli archi                 | $O(mlog(m))$                   |
| $n$ `makeset`                      | $O(n)$                         |
| Fino a $2m$ `find` + $n-1$ `union` | $O(m\alpha(m,n)) \approx O(m)$ |
**Totale:** $O(mlog(n))$ 

# Algoritmo di Prim
L'Algoritmo di Prim costruisce l' MST partendo da un singolo nodo e crescendo verso l'esterno, un po' come se "espandesse" una rete.

>[!Pensiero]
>Parto da un vertice e ogni volta aggiungo l'arco piú economico che collega un nodo dentro l'albero a un nodo fuori

È un approccio **top-down** (parte da un nodo e cresce).

## Passi dell'algoritmo
1. Scegli un nodo iniziale $s$ (sorgente)
2. Inizializza:
	- Un insieme $S = {s}$ (insieme dei nodi giá connessi)
	- Un insieme $V ∖ S$ (insieme dei nodi che non sono ancora stati aggiunti)
3.  Ad ogni passo:
	- Trova l'arco piú economico che collega un nodo in $S$ con uno in $V ∖ S$;
	- Aggiungi l'arco e il nuovo nodo a $S$.
4. Ripeti finché tutti i nodi non sono includi.

## Pseudo-Codice
```Pseudo
Prim(G, s):
    per ogni vertice v:
        a[v] = ∞
    a[s] = 0
    Q = priority queue contenente tutti i vertici
    T = ∅
    mentre Q non è vuota:
        u = deleteMin(Q)
        per ogni arco (u, v):
            se v ∈ Q e c(u,v) < a[v]:
                a[v] = c(u,v)
                parent[v] = u
                decreaseKey(Q, v)
    return T = {(v, parent[v]) per tutti i v}
```

### Complessitá dell'algoritmo
La complessitá dipende da come viene gestita la coda con prioritá:
Se la coda viene implementata con un Array:
	**Costo:** $O(n^{2})$
Se la coda viene implementata con un Heap Binario:
	**Costo:** $O(mlog(n))$
Se la coda viene implementata con un Heap di Fibonacci:
	**Costo:** $O(m + nlog(n))$

**Quindi:** 
	usando l'Heap di Fibonacci il costo totale finale sará $O(mlog(n))$

## Esempio Reale
Immaginare una rete elettrica:
Si inizia da una centrale (nodo A) e aggiungi cavi piú economici che raggiungono altri edifici, senza mai creare cicli

# Differenze principali tra Kruskal e Prim

| Aspetto                     | Prim                                         | Kruskal                                              |
| --------------------------- | -------------------------------------------- | ---------------------------------------------------- |
| Approccio                   | Cresce un singolo albero (Top-Down)          | Unisce piú foreste (Bottom-Up)                       |
| Inizio                      | Da un nodo qualsiasi del grafo               | Da tutti verticic separati                           |
| Scelta Greedy               | Arco piú economico che collega un nuovo nodo | Arco  piú economico che collega due insiemi distinti |
| Struttura dati              | Priority Queue (Migliore: Heap di Fibonacci) | Union-Find                                           |
| Numero di archi controllati | Tutti, ma gestiti tramite Heap               | Tutti, ordinati dall'inizio                          |
| Complessitá                 | $O(mlog(n))$                                 | $O(mlog(n))$                                         |
| MIgliore per...             | Grafi con molti archi                        | Grafi con pochi archi                                |
|                             |                                              |                                                      |
## Finale
- **Kruskal**: aggiunge archi in ordine crescente, unendo foreste → perfetto per grafi **sparsi**.
- **Prim**: espande un singolo albero da un nodo → perfetto per grafi **densi**.
- Entrambi danno **lo stesso MST** (se il grafo è connesso).
- Le differenze stanno solo nell’approccio e nei dettagli implementativi.