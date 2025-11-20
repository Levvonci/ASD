### HeapSort: Descrizione e Funzionamento

HeapSort è un algoritmo di ordinamento basato su una struttura dati chiamata heap (ammasso). Un heap è una struttura dati completa ad albero binario che soddisfa la proprietà dell'heap: in un max-heap, ogni nodo genitore è maggiore o uguale ai suoi figli; in un min-heap, ogni nodo genitore è minore o uguale ai suoi figli.

HeapSort utilizza un max-heap per ordinare gli elementi in ordine crescente. L'idea di base è costruire un max-heap dall'array, quindi estrarre l'elemento massimo (la radice del heap) e metterlo alla fine dell'array, riducendo la dimensione del heap di uno, e ripetere il processo.

### Passaggi dell'algoritmo HeapSort

1. **Costruire il max-heap**: Riarrangia l'array in modo che soddisfi la proprietà del max-heap.
2. **Estrarre elementi dal heap**: Scambia la radice del heap con l'ultimo elemento del heap e riduci la dimensione del heap di uno. Richiama la funzione heapify per ripristinare la proprietà del heap.
3. **Ripetere**: Ripeti il processo finché tutti gli elementi sono stati estratti e ordinati.

### Pseudocodice

Ecco lo pseudocodice per HeapSort:

```plaintext
function heapSort(A):
    n = length(A)

    # Costruire il max-heap
    for i = n / 2 - 1 to 0 do
        heapify(A, n, i)

    # Estrarre elementi dal heap uno alla volta
    for i = n - 1 to 0 do
        swap(A[0], A[i])
        heapify(A, i, 0)

function heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] > A[largest]:
        largest = left

    if right < n and A[right] > A[largest]:
        largest = right

    if largest != i:
        swap(A[i], A[largest])
        heapify(A, n, largest)
```

### Spiegazione del Pseudocodice

1. **Funzione `heapSort`**:
   - Calcola la lunghezza dell'array `n`.
   - Costruisce il max-heap partendo dall'ultimo nodo non foglia e andando verso l'inizio dell'array.
   - Estrae gli elementi dal heap uno alla volta, scambiando la radice del heap con l'ultimo elemento del heap e riducendo la dimensione del heap di uno. Chiama `heapify` per ripristinare la proprietà del heap.

2. **Funzione `heapify`**:
   - Assume che l'albero binario radicato nell'indice `i` sia un heap, ad eccezione del nodo `i`.
   - Confronta il nodo `i` con i suoi figli sinistro e destro.
   - Se uno dei figli è maggiore del nodo `i`, scambia il nodo `i` con il figlio maggiore e richiama `heapify` ricorsivamente sul sotto-albero interessato.
