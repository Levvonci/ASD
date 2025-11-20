def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contare le occorrenze delle cifre
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Cambiare count[i] in posizione effettiva di questa cifra nell'output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Costruire l'array di output
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copiare l'array di output nell'array originale, così che arr sia ordinato per questa cifra
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if len(arr) == 0:
        return arr

    # Trovare il massimo numero per sapere il numero di cifre
    max_num = max(arr)

    # Eseguire il counting sort per ogni cifra (unità, decine, centinaia, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array originale:", arr)
    radix_sort(arr)
    print("Array ordinato:", arr)

'''
    Funzione counting_sort_by_digit:
        Conta le occorrenze di ogni cifra per la cifra attuale (determinata da exp).
        Modifica count per rappresentare le posizioni effettive di ogni cifra nell'array ordinato.
        Costruisce l'array di output ordinato per la cifra attuale.
        Copia l'array di output nell'array originale per prepararsi all'ordinamento della prossima cifra.

    Funzione radix_sort:
        Trova il numero massimo nell'array per determinare il numero di cifre.
        Esegue il CountingSort per ogni cifra, iniziando dalle unità fino alla cifra più significativa, incrementando exp per passare alla cifra successiva.

    Esempio di Utilizzo:
        Crea un array di esempio arr.
        Chiama la funzione radix_sort su di esso.
        Dopo l'esecuzione di radix_sort, l'array sarà ordinato e stampato.

Complessità

    Tempo:
        Migliore: O(nk)O(nk)
        Medio: O(nk)O(nk)
        Peggiore: O(nk)O(nk)

    Dove nn è il numero di elementi e kk è il numero di cifre del numero massimo.

    Spazio: O(n+k)O(n+k) (per i bucket e l'array di output)

RadixSort è un algoritmo di ordinamento molto efficiente per numeri interi quando kk (il numero di cifre) è relativamente piccolo rispetto a nn. Tuttavia, non è adatto per ordinare numeri con una grande gamma di valori o per ordinare tipi di dati complessi.
'''
