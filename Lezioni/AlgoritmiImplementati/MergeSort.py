def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2 #trovo il centro dividendo l'array a metà

        L = arr[:mid] #array di sinistra
        R = arr[mid:] #array di destra

        merge_sort(L) #ordina l'array di sinistra 
        merge_sort(R) #ordina l'array di destra

        i = j = k = 0

        #copio i dati negli array temporanei L[] e R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Controlla se qualche elemento è rimasto
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [13, 22, 21, 10, 48, 2, 89, 2, 56, 3]
print("Array iniziale:", arr)
merge_sort(arr)
print("Array ordinato:", arr)

