é un problema in cui dati $j$ jobs con starting time $s_{i}$ e finish time $f_{i}$, l'obiettivo é trovare il sottoinsieme $S$ massimale di jobs compatibili tra loro.
due job non si sovrappongono se il finish time del primo job é <= dello starting time del secondo job

## Algoritmo ottimale - Earliest finish time first
1. ordino i j jobs ib base al loro finish time
2. inizializzo il sottoinsieme S
3. scorro i jobs dal primo all'ultimo
	4. se il job che sto vedendo é compatibile con S
		5. allora inserisco il job all'interno di S
	5. Altrimenti no
4. Restituisco S
Ordinare $n$ jobs costa $O(nlog(n))$ con algoritmo di sorting
Inserimento del job all'interno del sottoinsieme $S$ costo $O(1)$
Decidere quale job inserire $O(n)$
Costo totale dell'algoritmo $O(nlog(n))$

## Dimostrazione di correttezza
Siano $i_{1}, \dots, i_{k}$ l'insieme di jobs appartenenti all'algoritmo greedy
Siano $j_{1},\dots, j_{k}$ l'insieme di job appartenenti all'algoritmo ottimo

Assumiamo che il greedy non é ottimale, ovvero $m > k$.
$\implies$ $\exists$ un ulteriore job nella soluzione ottima che viene schedulato, ma se esistesse un job schedulabile allora l'algoritmo greedy avrebbe dovuto prenderlo considerando che i jobs sono ordinati per finish time.
Quindi: il Greedy è ottimo
