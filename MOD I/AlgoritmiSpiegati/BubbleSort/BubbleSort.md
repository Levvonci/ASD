### BubbleSort: Descrizione e Funzionamento

BubbleSort è un semplice algoritmo di ordinamento basato sul confronto e lo scambio di coppie di elementi adiacenti. Il nome deriva dal modo in cui gli elementi "bolla" salgono alla loro posizione corretta, come bolle d'aria che emergono in superficie.

### Passaggi dell'algoritmo BubbleSort

1. **Iterare attraverso l'array**: Scorri l'array più volte.
2. **Confrontare coppie adiacenti**: Confronta ogni coppia di elementi adiacenti.
3. **Scambiare se necessario**: Se un elemento è maggiore del successivo, scambiali.
4. **Ripetere**: Ripeti i passaggi fino a quando l'array è ordinato.

### Pseudocodice

Ecco lo pseudocodice per BubbleSort:

```plaintext
function bubbleSort(A):
    n = length(A)
    for i = 0 to n-1 do
        for j = 0 to n-i-2 do
            if A[j] > A[j+1] then
                swap A[j] with A[j+1]
```

### Spiegazione del Pseudocodice

1. **Funzione `bubbleSort`**:
   - Si calcola la lunghezza dell'array `n`.
   - Si esegue un ciclo esterno da 0 a `n-1`.
   - All'interno del ciclo esterno, si esegue un ciclo interno da 0 a `n-i-2`.
   - Per ogni coppia di elementi adiacenti, se il primo elemento è maggiore del secondo, vengono scambiati.

