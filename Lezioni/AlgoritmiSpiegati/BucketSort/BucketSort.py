def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # 1. Creare i bucket
    bucket_count = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / bucket_count
    buckets = [[] for _ in range(bucket_count)]

    # 2. Distribuire gli elementi nei bucket
    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index == bucket_count:  # Fix edge case where num is max_value
            index -= 1
        buckets[index].append(num)

    # 3. Ordinare ogni bucket
    for bucket in buckets:
        insertion_sort(bucket)

    # 4. Concatenare i bucket ordinati
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

if __name__ == "__main__":
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Array originale:", arr)
    sorted_arr = bucket_sort(arr)
    print("Array ordinato:", sorted_arr)

'''
    Funzione insertion_sort:
        Implementa l'algoritmo di ordinamento InsertionSort per ordinare i singoli bucket.

    Funzione bucket_sort:
        Controlla se l'array è vuoto.
        Calcola il numero di bucket come la lunghezza dell'array.
        Determina il valore massimo e minimo dell'array.
        Calcola l'intervallo del bucket.
        Crea un numero di bucket vuoti.
        Distribuisce ogni elemento dell'array originale nel bucket appropriato.
        Ordina individualmente ogni bucket utilizzando insertion_sort.
        Concatenare gli elementi ordinati di tutti i bucket per ottenere l'array finale ordinato.

    Esempio di Utilizzo:
        Crea un array di esempio arr.
        Chiama la funzione bucket_sort su di esso.
        Dopo l'esecuzione di bucket_sort, l'array sarà ordinato e stampato.

Complessità

    Tempo:
        Migliore: O(n+k)O(n+k)
        Medio: O(n+k)O(n+k)
        Peggiore: O(n2)O(n2) (se tutti gli elementi finiscono nello stesso bucket e l'algoritmo di ordinamento usato nei bucket è O(n2)O(n2))
    Spazio: O(n+k)O(n+k) (per i bucket aggiuntivi)

BucketSort è particolarmente efficiente quando gli elementi sono distribuiti uniformemente e quando il numero di bucket è scelto correttamente. Tuttavia, la sua efficienza può diminuire se gli elementi non sono distribuiti uniformemente o se il numero di bucket non è ottimale.
'''

