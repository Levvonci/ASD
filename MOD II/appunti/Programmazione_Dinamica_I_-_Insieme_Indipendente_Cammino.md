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




