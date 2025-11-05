é un problema in cui dati j jobs con starting time e finish time l'obiettibvo é trovare il sottoinsieme massimale di jobs compatibili tra loro
due job non si sovrappongono se il finish time del primo job é <= dello starting time del secondo job

## Algoritmo ottimale
1. ordino i j jobs ib base al loro finish time
2. inizializzo il sottoinsieme S
3. scorro i jobs dal primo all'ultimo
	4. se il job che sto vedendo é compatibile con S
		5. allora inserisco il job all'interno di S
	5. Altrimenti no
4. Restituisco S
Ordinare n jobs costa O(nlog(n)) con algoritmo di soprting
Inserimento del job all'interno del sottoinsieme S costo O(1)
Decidere quale job inserire O(n)
Costo totale dell'algoritmo O(nlog(n))

## Dimostrazione di correttezza
siano i1, .... ik l'insieme di jobs appartenenti all'algoritmo greedy
siano j1, ...., jk l'insieme di job appartenenti all'algoritmo ottimo

Assumiamo che il greedy non é ottimale, ovvero k < m
e dimostriamo che ció non é possibile.
