def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Array originale:", arr)
    bubble_sort(arr)
    print("Array ordinato:", arr)

'''
    Funzione bubble_sort:
        Calcola la lunghezza dell'array n.
        Esegue un ciclo esterno da 0 a n-1.
        Esegue un ciclo interno da 0 a n-i-1.
        Confronta ogni coppia di elementi adiacenti. Se il primo è maggiore del secondo, li scambia.

    Esempio di Utilizzo:
        Crea un array di esempio arr.
        Chiama la funzione bubble_sort su di esso.
        Dopo l'esecuzione di bubble_sort, l'array sarà ordinato e stampato.

Complessità

    Tempo:
        Migliore: O(n)O(n) (quando l'array è già ordinato)
        Medio: O(n2)O(n2)
        Peggiore: O(n2)O(n2)
    Spazio: O(1)O(1) (in-place, nessuna memoria aggiuntiva richiesta)

BubbleSort è facile da implementare e comprendere, ma è inefficiente per grandi dataset a causa della sua complessità temporale quadratica. È adatto principalmente per dataset piccoli o per scopi didattici.
'''
