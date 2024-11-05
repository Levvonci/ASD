def bubble_sort(arr):
    n = len(arr) 
    for i in range (n): #Con un indice scorro la lunghezza dell'array
        for j in range (0, n-i-1): #Con j punto gli elementi per scambiarli
            if arr[j] > arr[j+1]: #Se l'elemento in posizione j è > di j+1
                arr[j], arr[j+1] = arr[j+1], arr[j] #Allora scambio gli elementi spostando l'elemento j+1 nella posizione j

arr = [34, 15, 22, 89, 21, 99, 100]
bubble_sort(arr)
print(arr)

'''
Quanto costa questo algoritmo?
n^2
'''
