L'Interval partitioning è un problema dove troviamo $j$ lezioni, con starting time $s_{j}$ e finish time $f_{j}$. L'obiettivo è trovare il minimo numero di classi necessarie per schedulare tutte le lezioni in maniera tale che dentro ogni singola classe, le lezioni non si overlappino.

## Algoritmo Ottimale - Earlist start time first
```
1. Ordino i Jobs per starting time
2. inizializzo le classi a 0
3. Scorro le lezioni
	4. Se la lezione è schedulabile nella classe
		5. Allora la inserisco nella classe 
	5. Altrimenti
			1. Alloco una nuova classe e schedulo la lezione all'interno di              quella classe
```
Ordinare i jobs per starting time con un algoritmo di sorting costa $O(nlog(n))$ 
Le classi sono implementate con una coda con priorità (chiave: finish time dell'ultima lezione)
- Per allocare una nuova classe, uso l'INSERT all'interno della coda con priorità
- Per schedulare la lezione $j$ all'interno della classe $k$, incremento la chiave della classe $k$ con $f_{j}$ (finish time dell'ultima lezione schedulata)
- Per determinare quale lezione $j$ è compatibile con una classe, compariamo $s_{j}$ con con Find-Min
Il totale delle operazioni di coda con priorità è $O(n)$; ognugna impiega $O(log(n))$ tempo

## Chiave
**Depth:** massimo numero di intervalli che si sovrappongono in un certo istante
**Osservazione chiave:** Numero di classi che servono >= profondità

## Dimostrazione di Correttezza
Sia $d$ il numero di classi che l'algoritmo alloca.
La classe $d$ è aperta perchè bisogna schedulare una lezione chiamata $j$ che è icompatibile con le $d-1$ classi.
Dato che abbiamo ordinato per starting time tutte le lezioni, allora tutte le lezioni incompatibili inizieranno non più tardi di $s_{j}$.

depth massimo numero di intervalli che si sovrappongono in un certo istante