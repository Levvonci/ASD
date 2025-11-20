def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Array originale:", arr)
    insertion_sort(arr)
    print("Array ordinato:", arr)

'''
    Funzione insertion_sort:
        Calcola la lunghezza dell'array n.
        Esegue un ciclo da 1 a n.
        Per ogni elemento key a partire dal secondo, confronta key con gli elementi precedenti.
        Sposta gli elementi maggiori di key una posizione verso destra.
        Inserisce key nella sua posizione corretta.

    Esempio di Utilizzo:
        Crea un array di esempio arr.
        Chiama la funzione insertion_sort su di esso.
        Dopo l'esecuzione di insertion_sort, l'array sarà ordinato e stampato.

Complessità

    Tempo:
        Migliore: O(n)O(n) (quando l'array è già ordinato)
        Medio: O(n2)O(n2)
        Peggiore: O(n2)O(n2)
    Spazio: O(1)O(1) (in-place, nessuna memoria aggiuntiva richiesta)

InsertionSort è un algoritmo semplice e intuitivo, adatto per piccoli dataset o per array che sono già quasi ordinati. La sua complessità temporale quadratica lo rende inefficiente per grandi dataset.
'''
