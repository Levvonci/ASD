### InsertionSort: Descrizione e Funzionamento

InsertionSort è un semplice algoritmo di ordinamento che costruisce l'array ordinato uno alla volta, inserendo ogni nuovo elemento nella posizione corretta rispetto agli elementi già ordinati. È simile al modo in cui le persone ordinano le carte in mano.

### Passaggi dell'algoritmo InsertionSort

1. **Iterare attraverso l'array**: Inizia dal secondo elemento e attraversa l'array.
2. **Inserire l'elemento**: Per ogni elemento, confrontalo con gli elementi precedenti e spostali di una posizione verso destra fino a trovare la posizione corretta per l'elemento corrente.
3. **Ripetere**: Ripeti il processo per tutti gli elementi dell'array.

### Pseudocodice

Ecco lo pseudocodice per InsertionSort:

```plaintext
function insertionSort(A):
    n = length(A)
    for i = 1 to n-1 do
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key do
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
```

### Spiegazione del Pseudocodice

1. **Funzione `insertionSort`**:
   - Calcola la lunghezza dell'array `n`.
   - Esegue un ciclo da 1 a `n-1`.
   - Per ogni elemento, lo salva come `key` e confronta `key` con gli elementi precedenti.
   - Sposta gli elementi maggiori di `key` una posizione verso destra.
   - Inserisce `key` nella sua posizione corretta.
