# Il Problema: Insieme indipendente di peso massimo su un cammino
Si ha un grafo che é semplicemente un cammino lineare:
```
v1 — v2 — v3 — … — vn
```
Ogni nodo ha un peso $W_{i}.$

<u>Obiettivo:</u>
Trovare un sottoinsieme di nodi $S \subseteq V$ tale che:
1. Nessuna coppia di nodi in $S$ é collegata (Non sono adiacenti)
2. La somma dei pesi $w(S) = \sum_{v_{i} \in S} W_{i}$ sia massima possibile

In poche parole, bisogna scegliere dei nodi non consecutivi che massimizzano la somma dei pesi.

## Esempio:
```pseudo
Nodi:  v1 v2 v3 v4 v5 v6
Pesi:   1  4  8  4  3 10
```
Alcuni possibili:
- `{v1, v3, v5}` $\rightarrow$ peso 1 + 8 + 3 = 12
- `{v2, v4, v6}` $\rightarrow$ peso 4 + 4 + 10 = 18
- `{v1, v3, v6}` $\rightarrow$ peso 1 + 8 + 10 = 19 $\rightarrow$ Ottimo

## Perché i classici approcci non funzionano?
**Forza Bruta:**
- Generiamo tutti i sottoinsiemi possibili dei nodi $\rightarrow$ esistono $2^{n}$ combinazioni
- Per ognuno controlli se é indipendente e calcoli il peso.

**Complessitá:** $O(2^{n})$, troppo lenta anche per numeri piccoli.

**Greedy:**
Scegli sempre il nodo piú pesante non adiacente a quello che é stato appena scelto.

Funziona per alcuni esempi ma non sempre:
```pseudo
Pesi: 1  4  5  4
```
Greedy prenderebbe `{v3} = 5` perché é l'arco di peso massimo.
Meglio `{v2, v4} = 4 + 4 = 8`

Quindi Greedy non corretto.

**Divide et Impera:**
Divido il grafo a metá, risolvo i due lati e unisco le soluzioni.

Non funziona perché i due sotto-cammini possono interferire ai confini.
Se prendo l'ultimo nodo della primá metá e il primo nodo della secondá metá potrebbero essere adiacenti e la combinazione é invalida.

Quindi Divide et Impera scartata.

## Capire la struttura del problema
Qui arriva l'intuizione fondamentale della programmazione dinamica:
>[!Important]
>Capire come la soluzione ottima dipenda dalle soluzioni piú piccole

### Osservazione
Considera il nodo finale $v_{n}$.
Nella soluzione ottima $S^{*}$ ci sono solo due casi possibili:
1. $v_{n} \notin S^{*}$ $\implies$ $S^{*}$ è anche la soluzione ottima per i primi $n-1$ nodi
2. $v_{n} \in S^{*}$ $\implies$ $v_{n-1}$ non può essere in $S^{*}$ $\implies$ $S^{*} ∖ \{v_{n}\}$ è la soluzione ottima per i primi $n-2$ nodi

### Relazione ricorsiva
Definiamo $OPT[j]$ = peso dell'insieme indipendente ottimo per i primi $j$ nodi.
Allora:
$$OPT[j] = max (OPT[j-1], w_{j} + OPT[j-2])$$
Con casi base:
$$OPT[1] = w_{1}, \ OPT[2] = max(w_{1}, w_{2})$$ 
### Da ricorsione a iterazione
La ricorsione diretta (senza memorizzare risultati) sarebbe ancora esponenziale:
$$T(n) = T(n-1) + T(n-2)$$
$\rightarrow$ cresce come **Fibonacci**

## Algoritmo in forma iterativa
```pseudo
1. OPT[1] = w1
2. OPT[2] = max(w1, w2)
3. for j = 3 to n:
       OPT[j] = max( OPT[j-1], wj + OPT[j-2] )
4. return OPT[n]
```

**Complessità:**
- Tempo: $O(n)$ 
- Spazio: $O(n)$ (ma potrebbe eseere ridotto a $O(1)$ mantenendo solo gli ultimi 2 valori)

### Esempio
```pseudo
Pesi:   1  4  8  4  3 10
Indice: 1  2  3  4  5  6
```

| $j$ | $w_{j}$ | $OPT[j-1]$ | $w_{j} + OPT[j-2]$ | $OPT[j]$  |
| --- | ------- | ---------- | ------------------ | --------- |
| 1   | 1       | -          | -                  | 1         |
| 2   | 4       | -          | -                  | 4         |
| 3   | 8       | 4          | 8 + 1 = 9          | 9         |
| 4   | 4       | 9          | 4 + 4 = 8          | 9         |
| 5   | 3       | 9          | 3 + 9 = 12         | 12        |
| 6   | 10      | 12         | 10 + 9 = 19        | 19 Ottimo |
$\rightarrow$ il peso massimo è 19 (insieme `{v1, v3, v6}`)

## Ricostruire la soluzione
L'algoritmo calcola solo il valore ottimo.
Ma per sapere quali sono i nodi scelti, serve una seconda passata:
```pseudo
S* = ∅
j = n
while j ≥ 3:
    if OPT[j-1] ≥ wj + OPT[j-2]:
        j = j - 1
    else:
        S* = S* ∪ {vj}
        j = j - 2
if j == 2 and w2 > w1:
    S* = S* ∪ {v2}
else:
    S* = S* ∪ {v1}
return S*
```

**Complessità:**
$O(n)$ anche per la ricostruzione

# Principi generali della programmazione dinamica
1. Definire i sottoproblemi giusti
	- Devono essere pochi (Tipicamente $O(n), O(n^{2})$)
	- E facili da risolvere partendo da casi base
2. Trovare una relazione di ricorrenza
	- Esprimere la soluzione del problema grande in funzione dei sottoproblemi più piccoli.
3. Memorizzare
	- Evitare di ricalcolare più volte lo stesso problema
4. Definire un ordine di calcolo
	- I sottoproblemi piccoli devono essere risolti prima di quelli grandi

# Problema dei dipendenti aziendale alla festa
