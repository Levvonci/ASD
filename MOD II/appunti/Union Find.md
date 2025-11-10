Struttura dati che mantiene una collezione di insiemi disgiunti che a loro volta contengono tutti elementi distinti.
Possono essere eseguite 3 operazioni:
- **makeSet(x):** Crea un nuovo insieme di nome x con al suo interno l'elemento x
- **Union(A,B):** Unisce i due insiemi in un unico insieme con elemento rappresentativo A
- **find(x):** Restituisce il nome dell'elemento rappresentativo dell'insieme che contiene l'elemento x

# Approcci con alberi
Gli insiemi sono rappresentati come alberi radicati.
La radice é l'elemento rappresentativo dell'insieme.
Esistono due strategie rappresentative:
- **QuickFind**
- **QuickUnion**

## QuickFind
Alberi di altezza massima = 1
Radice = nome dell'insieme
Foglie = elementi (incluso l'elemento rappresentativo)

### Operazioni
- **makeSet(x):** Crea l'albero composto da due nodi, radice e figlio. Memorizza x sia nella radice, sia come elemento foglia - **Costo:** $O(1)$
- **Union(A,B):** Sostituisce tutti i puntatori dalle foglie di B alla radice A ed elimina la vecchia radice B - **Costo:** $O(n)$
- **find(x):** Restituisce l'elemento radice dell'albero che contiene l'elemento x - **Costo:** $O(1)$

**E se eseguo una sequenza arbitraria di operazioni?**

find e makeSet richiedono tempo costante, ma particolari sequenze di union possono essere inefficienti.
Se eseguo una sequenza di n-1 union con n alberi di altezza 1, la complessitá é un $\Theta(n^{2})$

## Migliorare QuickFind - Union By Size
Il miglioramento sta nel verificare la cardinalitá dei due insiemi.
**union(A,B)**
	se size(A) < size(B):
		allora cambio tutti i puntatori da A a B e modifico la radice nella maniera piú opportuna

**Quanto costa cambiare padre?** costante
**Quante volte puó cambiare padre un nodo?** al piú $log(n)$

Ogni volta che un elemento cambia padre, la cardinalitá dell'insieme al quale apparterrá é almeno doppia rispetto all'insieme di partenza.
- All'inizio un nodo é un insieme di dimensione 1
- Se cambia padre, l'insieme é di dimensione almeno 2
- All'i-esimo cambio é un insime di dimensione almeno 2$^{i}$ 
Il tempo speso per un singolo nodo sull'intera sequenza di n union é $O(log(n))$
Il costo totale infine é $O(nlog(n))$ 

## QuickUnion
Alberi di altezza massima > 1
Radice = elemento rappresentativo dell'insieme
Nodi rimanenti = altri elementi escluso l'elemento radice

### Operazioni
- **makeSet(x):** Crea l'albero composto da 1 nodo, la radice. - **Costo:** $O(1)$
- **Union(A,B):** Unisco i singoli nodi - **Costo:** $O(1)$
- **find(x):** Restituisco l'elemento effettivo che ricerco all'interno di un albero - **Costo:** $O(n)$ - **Perché?:** devo scorrere tutto l'albero per trovare l'elemento

**E se eseguo una sequenza arbitraria di operazioni?**

particolari sequenze di union possono generare un albero di altezza lineare, quindi questo renderebbe una find molto inefficiente.
n makeset, n-1 union seguite da m find richiederebbero un costo di $O(n+n-1+nm) = O(nm)$

## Migliorare QuickUnion - Union By Size
Il miglioramento sta nel verificare la size degli alberi.
Rendiamo la radice dell'albero con meno nodi figlia della radice dell'albero con piú nodi.

Con la Union By Size, dato un albero QuickUnion con size $s$ e altezza $h$, vale che $s \geq 2^{h}$ 

## Compressione dei Cammini
quando eseguo find(x) e attraverso il cammino da x alla
radice, comprimo il cammino, ovvero rendo tutti i nodi del
cammino figli della radice.
La prima find costerá sempre lineare, ma le prossime find con cammini compressi costeranno di meno.