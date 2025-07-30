### RadixSort: Descrizione e Funzionamento

RadixSort è un algoritmo di ordinamento non comparativo che ordina i numeri processando una cifra alla volta. L'idea di base è ordinare i numeri iniziando dalla cifra meno significativa fino a quella più significativa, utilizzando un algoritmo di ordinamento stabile come CountingSort per ordinare le cifre individualmente.

### Passaggi dell'algoritmo RadixSort

1. **Determinare il numero massimo**: Trova il numero con il maggior numero di cifre nell'array.
2. **Ordinare le cifre**: Per ogni cifra, dall'unità alle cifre più significative, ordina l'array utilizzando CountingSort.

### Pseudocodice

Ecco lo pseudocodice per RadixSort:

```plaintext
function radixSort(A):
    d = massimo numero di cifre in A
    for i = 1 to d do
        A = countingSortByDigit(A, i)
    return A

function countingSortByDigit(A, digit):
    n = length(A)
    output = array of n zeros
    count = array of 10 zeros

    # Calcolare la posizione delle cifre
    for j = 0 to n-1 do
        digit_of_Aj = (A[j] / 10^(digit-1)) % 10
        count[digit_of_Aj] = count[digit_of_Aj] + 1

    # Calcolare gli indici per l'output
    for j = 1 to 9 do
        count[j] = count[j] + count[j-1]

    # Costruire l'array di output
    for j = n-1 downto 0 do
        digit_of_Aj = (A[j] / 10^(digit-1)) % 10
        output[count[digit_of_Aj] - 1] = A[j]
        count[digit_of_Aj] = count[digit_of_Aj] - 1

    return output
```

### Spiegazione del Pseudocodice

1. **Funzione `radixSort`**:
   - Trova il numero di cifre massime (`d`) nell'array.
   - Per ogni cifra dall'unità alle cifre più significative, ordina l'array utilizzando `countingSortByDigit`.

2. **Funzione `countingSortByDigit`**:
   - Conta le occorrenze di ogni cifra per la cifra specifica.
   - Calcola le posizioni corrette per ogni elemento nell'array ordinato.
   - Costruisce l'array di output ordinato per la cifra specifica.