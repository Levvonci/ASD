def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n - 1)
    print("Array ordinato è:", arr)

'''
    Funzione quicksort:
        Se low è minore di high, si chiama la funzione partition per ottenere l'indice del pivot.
        Si eseguono chiamate ricorsive a quicksort per ordinare le sotto-sezioni dell'array prima e dopo il pivot.

    Funzione partition:
        Il pivot è scelto come l'ultimo elemento dell'array.
        Si riordina l'array in modo che tutti gli elementi minori o uguali al pivot siano a sinistra e gli elementi maggiori a destra.
        Si ritorna l'indice finale del pivot.

    Esempio di Utilizzo:
        Si crea un array di esempio arr e si chiama quicksort su di esso.
        Dopo l'esecuzione di quicksort, l'array sarà ordinato e stampato.

Questa implementazione di QuickSort è in-place, cioè ordina l'array senza utilizzare memoria aggiuntiva significativa, e ha una complessità temporale media di O(nlog⁡n)O(nlogn). Tuttavia, nel peggiore dei casi (quando l'array è già ordinato o quasi ordinato), la complessità temporale è O(n2)O(n2).
'''                                                                                                    
