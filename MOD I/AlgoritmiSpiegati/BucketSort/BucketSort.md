### BucketSort: Descrizione e Funzionamento

BucketSort è un algoritmo di ordinamento che suddivide un array in un numero di sotto-array (bucket) e poi ordina questi bucket individualmente, sia utilizzando un altro algoritmo di ordinamento, sia ricorsivamente applicando BucketSort. Questo algoritmo è particolarmente efficace quando gli elementi sono distribuiti uniformemente su un intervallo.

### Passaggi dell'algoritmo BucketSort

1. **Creare i bucket**: Dividere l'intervallo dei valori in un numero di bucket.
2. **Distribuire gli elementi**: Inserire ogni elemento dell'array originale nel bucket appropriato.
3. **Ordinare i bucket**: Ordinare individualmente ciascun bucket.
4. **Concatenare i bucket**: Unire gli elementi ordinati di tutti i bucket per ottenere l'array ordinato finale.

### Pseudocodice

Ecco lo pseudocodice per BucketSort:

```plaintext
function bucketSort(A, k):
    n = length(A)
    B = array of k empty buckets

    # Distribuire gli elementi nei bucket
    for i = 0 to n-1 do
        index = floor(k * A[i])
        B[index].append(A[i])

    # Ordinare ogni bucket
    for i = 0 to k-1 do
        B[i] = sort(B[i])

    # Concatenare i bucket ordinati
    result = []
    for i = 0 to k-1 do
        result.extend(B[i])

    return result
```

### Spiegazione del Pseudocodice

1. **Funzione `bucketSort`**:
   - Calcola la lunghezza dell'array `n`.
   - Crea un array `B` di `k` bucket vuoti.
   - Distribuisce ogni elemento dell'array originale nel bucket appropriato, utilizzando una funzione di hashing semplice (ad esempio, `floor(k * A[i])`).
   - Ordina individualmente ogni bucket. Può essere utilizzato un algoritmo di ordinamento semplice come InsertionSort.
   - Concatenare gli elementi ordinati di tutti i bucket per ottenere l'array finale ordinato.
