### QuickSort: Descrizione e Funzionamento

QuickSort è un algoritmo di ordinamento efficiente e ampiamente utilizzato che segue il paradigma divide-et-impera. Ecco come funziona:

1. **Scelta del Pivot**: Si sceglie un elemento dall'array come pivot.
2. **Partizionamento**: Si riordina l'array in modo che tutti gli elementi con valore minore del pivot vengano prima del pivot e tutti gli elementi con valore maggiore del pivot vengano dopo. Il pivot si trova quindi nella sua posizione finale.
3. **Ricorsione**: Si applica ricorsivamente la stessa procedura agli array sotto e sopra il pivot.

### Pseudocodice

Ecco lo pseudocodice per QuickSort:

```plaintext
function quicksort(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)
        quicksort(A, low, pivot_index - 1)
        quicksort(A, pivot_index + 1, high)

function partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j = low to high - 1:
        if A[j] <= pivot:
            i = i + 1
            swap A[i] with A[j]
    swap A[i + 1] with A[high]
    return i + 1
```

### Spiegazione del Pseudocodice

1. **Funzione `quicksort`**:
   - Se l'indice `low` è minore di `high`, si esegue il partizionamento per ottenere la posizione corretta del pivot.
   - Si chiamano ricorsivamente `quicksort` sulle due metà dell'array, escluse le posizioni del pivot.

2. **Funzione `partition`**:
   - Si sceglie l'ultimo elemento dell'array come pivot.
   - Si riordina l'array in modo che tutti gli elementi minori o uguali al pivot vengano prima e tutti quelli maggiori vengano dopo.
   - Si ritorna l'indice del pivot.

cva significativa, e ha una complessità temporale media di \(O(n \log n)\). Tuttavia, nel peggiore dei casi (quando l'array è già ordinato o quasi ordinato), la complessità temporale è \(O(n^2)\).
