def insertion_sort(arr):
    # Scorri dall'elemento 1 fino alla fine dell'array
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Sposta gli elementi di arr[0..i-1], che sono maggiori di key,
        # una posizione avanti rispetto alla loro posizione attuale
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Codice di test
arr = [11, 10, 9, 68, 9711, 10, 9, 68, 97, 0, 89, 2, 3, 99]
print("Array iniziale:", arr)
insertion_sort(arr)
print("Array ordinato:", arr)

