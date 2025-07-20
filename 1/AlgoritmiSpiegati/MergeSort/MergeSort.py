def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Array originale:", arr)
    merge_sort(arr)
    print("Array ordinato:", arr)

'''
    Funzione merge_sort:
        Se l'array ha più di un elemento, viene diviso in due metà L e R.
        Si chiama merge_sort ricorsivamente sulle due metà.
        Si fondono le due metà ordinate nell'array originale.

    Unione degli Array:
        Gli indici i, j, e k sono usati per attraversare rispettivamente gli array L, R, e l'array originale.
        Gli elementi di L e R vengono confrontati e l'elemento minore viene inserito nell'array originale.
        Una volta che tutti gli elementi di uno degli array temporanei sono stati inseriti, si copiano direttamente gli elementi rimanenti dell'altro array temporaneo nell'array originale.

Complessità

    Tempo:
        Migliore: O(nlog⁡n)O(nlogn)
        Medio: O(nlog⁡n)O(nlogn)
        Peggiore: O(nlog⁡n)O(nlogn)
    Spazio: O(n)O(n) a causa degli array temporanei utilizzati per la fusione.

MergeSort è un algoritmo efficiente e stabile, che garantisce una complessità temporale di O(nlog⁡n)O(nlogn) in tutti i casi, rendendolo ideale per l'ordinamento di grandi dataset.

'''
