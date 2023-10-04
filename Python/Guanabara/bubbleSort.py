lista = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10]
def bubble_sort(arr):
        n = len(arr)

        #para cada elemtno i do array
        for i in range(n):
            #para cada elemento j do array
            for j in range(0, n-i-1):
                #se o elemento i for maior que o elemento j
                if arr[j] > arr[j+1]:
                    #troca os elementos i e j
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

print(bubble_sort(lista))

