Il bucket sort è un algoritmo di ordinamento che distribuisce gli elementi di un array in una serie di "bucket" (contenitori). Ogni bucket è poi ordinato individualmente, spesso usando un altro algoritmo di ordinamento, come l'insertion sort. Infine, gli elementi ordinati vengono concatenati per formare l'array ordinato finale. Questo algoritmo è particolarmente efficiente quando gli elementi da ordinare sono distribuiti uniformemente.

### Passaggi dell'algoritmo Bucket Sort

1. **Creazione dei bucket**: Si crea un numero di bucket. Ogni bucket rappresenta un intervallo di valori.
2. **Distribuzione degli elementi**: Gli elementi dell'array vengono distribuiti nei bucket in base al loro valore.
3. **Ordinamento dei bucket**: Ogni bucket viene ordinato usando un altro algoritmo di ordinamento.
4. **Concatenazione dei bucket**: Gli elementi ordinati dei bucket vengono concatenati per formare l'array finale ordinato.

### Pseudocodice

Ecco uno pseudocodice per il bucket sort:

```plaintext
BucketSort(A)
  n = length(A)
  B = array of n empty buckets
  
  for i = 0 to n-1 do
    insert A[i] into bucket B[floor(n * A[i])]
  
  for i = 0 to n-1 do
    sort(B[i])
  
  k = 0
  for i = 0 to n-1 do
    for j = 0 to length(B[i]) - 1 do
      A[k] = B[i][j]
      k = k + 1
```

### Spiegazione dello pseudocodice

1. **Inizializzazione dei bucket**: Si crea un array `B` di `n` bucket vuoti.
2. **Distribuzione degli elementi**: Per ogni elemento `A[i]` nell'array originale, si calcola l'indice del bucket appropriato usando `floor(n * A[i])`. L'elemento viene quindi inserito nel bucket corrispondente.
3. **Ordinamento dei bucket**: Si ordinano i singoli bucket. Qui, si può usare un qualsiasi algoritmo di ordinamento; spesso si utilizza l'insertion sort per la sua efficienza su piccoli insiemi di dati.
4. **Concatenazione dei bucket**: Si concatenano gli elementi ordinati di ciascun bucket per formare l'array finale ordinato.

### Esempio

Consideriamo l'array `[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]`.

1. **Creazione dei bucket**: Si creano 10 bucket vuoti.
2. **Distribuzione degli elementi**:
   - `0.78` va nel bucket `7` (perché `floor(10 * 0.78) = 7`)
   - `0.17` va nel bucket `1`
   - `0.39` va nel bucket `3`
   - `0.26` va nel bucket `2`
   - `0.72` va nel bucket `7`
   - `0.94` va nel bucket `9`
   - `0.21` va nel bucket `2`
   - `0.12` va nel bucket `1`
   - `0.23` va nel bucket `2`
   - `0.68` va nel bucket `6`

3. **Ordinamento dei bucket**:
   - Bucket `1`: `[0.17, 0.12]` diventa `[0.12, 0.17]`
   - Bucket `2`: `[0.26, 0.21, 0.23]` diventa `[0.21, 0.23, 0.26]`
   - Bucket `3`: `[0.39]` (già ordinato)
   - Bucket `6`: `[0.68]` (già ordinato)
   - Bucket `7`: `[0.78, 0.72]` diventa `[0.72, 0.78]`
   - Bucket `9`: `[0.94]` (già ordinato)

4. **Concatenazione dei bucket**: `[0.12, 0.17]`, `[0.21, 0.23, 0.26]`, `[0.39]`, `[0.68]`, `[0.72, 0.78]`, `[0.94]` diventa `[0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]`.

### Complessità

- **Tempo**:
  - Migliore: \(O(n + k)\)
  - Medio: \(O(n + k)\)
  - Peggiore: \(O(n^2)\) (quando gli elementi non sono distribuiti uniformemente)
- **Spazio**: \(O(n + k)\), dove \(k\) è il numero di bucket.

Il bucket sort è efficace per insiemi di dati con una distribuzione uniforme e quando il numero di bucket è scelto correttamente.
