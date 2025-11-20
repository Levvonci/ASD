### MergeSort: Descrizione e Funzionamento

MergeSort è un algoritmo di ordinamento che segue il paradigma divide-et-impera. È stabile e ha una complessità temporale di \(O(n \log n)\) sia nel caso medio che nel caso peggiore. L'idea di base è dividere ricorsivamente l'array in due metà finché ogni sotto-array contiene un solo elemento, e poi unire (merge) le due metà ordinate.

### Passaggi dell'algoritmo MergeSort

1. **Dividere**: Dividere l'array in due metà.
2. **Ordinare**: Ordinare ricorsivamente ciascuna metà.
3. **Unire**: Unire le due metà ordinate per produrre l'array ordinato.

### Pseudocodice

Ecco lo pseudocodice per MergeSort:

```plaintext
function mergesort(A, left, right):
    if left < right:
        mid = (left + right) / 2
        mergesort(A, left, mid)
        mergesort(A, mid + 1, right)
        merge(A, left, mid, right)

function merge(A, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = array of size n1
    R = array of size n2

    for i = 0 to n1 - 1:
        L[i] = A[left + i]
    for j = 0 to n2 - 1:
        R[j] = A[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1

    while i < n1:
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j < n2:
        A[k] = R[j]
        j = j + 1
        k = k + 1
```

### Spiegazione del Pseudocodice

1. **Funzione `mergesort`**:
   - Se `left` è minore di `right`, si calcola il punto medio `mid`.
   - Si chiama `mergesort` ricorsivamente sulle due metà dell'array.
   - Si chiama la funzione `merge` per unire le due metà ordinate.

2. **Funzione `merge`**:
   - Si calcolano le dimensioni delle due metà dell'array e si creano array temporanei `L` e `R`.
   - Si copiano gli elementi dell'array originale nei rispettivi array temporanei.
   - Si fondono gli array temporanei nell'array originale in ordine crescente.

