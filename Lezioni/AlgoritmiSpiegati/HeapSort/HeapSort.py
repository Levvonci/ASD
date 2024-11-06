def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Costruire il max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Estrarre elementi dal heap uno alla volta
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Array originale:", arr)
    heap_sort(arr)
    print("Array ordinato:", arr)

'''
    Funzione heapify:
        Calcola l'indice del figlio sinistro (left) e del figlio destro (right).
        Confronta il nodo i con i suoi figli sinistro e destro.
        Se uno dei figli è maggiore del nodo i, scambia il nodo i con il figlio maggiore e richiama heapify ricorsivamente sul sotto-albero interessato.

    Funzione heap_sort:
        Calcola la lunghezza dell'array n.
        Costruisce il max-heap partendo dall'ultimo nodo non foglia e andando verso l'inizio dell'array.
        Estrae gli elementi dal heap uno alla volta, scambiando la radice del heap con l'ultimo elemento del heap e riducendo la dimensione del heap di uno. Chiama heapify per ripristinare la proprietà del heap.

    Esempio di Utilizzo:
        Crea un array di esempio arr.
        Chiama la funzione heap_sort su di esso.
        Dopo l'esecuzione di heap_sort, l'array sarà ordinato e stampato.

Complessità

    Tempo:
        Migliore: O(nlog⁡n)O(nlogn)
        Medio: O(nlog⁡n)O(nlogn)
        Peggiore: O(nlog⁡n)O(nlogn)
    Spazio: O(1)O(1) (in-place, nessuna memoria aggiuntiva richiesta)

HeapSort è un algoritmo di ordinamento molto efficiente con una complessità temporale garantita di O(nlog⁡n)O(nlogn) in tutti i casi. Tuttavia, a causa del suo comportamento di accesso casuale ai dati, può essere meno efficiente di altri algoritmi di ordinamento come QuickSort per determinati tipi di dati.
'''
