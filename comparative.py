import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)


def bubble_sort(file_name):
    with open(file_name, 'r') as archivo:
        numeros = [int(linea.strip()) for linea in archivo]

    n = len(numeros)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    with open(file_name, 'w') as archivo:
        for numero in numeros:
            archivo.write(str(numero) + '\n')  

def counting_sort(file_name):

    with open(file_name, 'r') as archivo:
        numeros = [int(linea.strip()) for linea in archivo]

    valor_maximo = max(numeros)

    conteo = [0] * (valor_maximo + 1)

    for numero in numeros:
        conteo[numero] += 1

    numeros_ordenados = []
    for i in range(len(conteo)):
        numeros_ordenados.extend([i] * conteo[i])

    with open(file_name, 'w') as archivo:
        for numero in numeros_ordenados:
            archivo.write(str(numero) + '\n')

def heap_sort(file_name):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def build_heap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    build_heap(numbers)
    sorted_numbers = []
    while numbers:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
        sorted_numbers.insert(0, numbers.pop())
        heapify(numbers, len(numbers), 0)

    with open(file_name, 'w') as file:
        for number in sorted_numbers:
            file.write(str(number) + '\n')

def insertion_sort(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def merge_sort(file_name):
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [arr[left + i] for i in range(n1)]
        R = [arr[mid + 1 + i] for i in range(n2)]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)

    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    merge_sort_helper(numbers, 0, len(numbers) - 1)

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')
 
def quick_sort(file_name):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    quick_sort_helper(numbers, 0, len(numbers) - 1)

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def selection_sort(file_name):    
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')       

                         
def calcular_tiempo_ejecucion(algoritmo, fileName):
    inicio = time.time()
    algoritmo(fileName)
    fin = time.time()
    return fin - inicio

def comparar_tiempos_algoritmos(nombres_archivos):
    tiempos = [[] for _ in range(7)]  # Lista de tiempos para cada algoritmo

    for nombre_archivo in nombres_archivos:      
        for i, algoritmo in enumerate([bubble_sort, counting_sort, heap_sort, insertion_sort, merge_sort, quick_sort, selection_sort]):
            tiempo = calcular_tiempo_ejecucion(algoritmo, nombre_archivo + '.txt')
            tiempos[i].append(tiempo)

    # Graficar los tiempos de ejecución
    algoritmos = ['Bubble Sort', 'Counting Sort', 'Heap Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort']

    for i in range(len(algoritmos)):
        plt.plot(nombres_archivos, tiempos[i], '-o', label=algoritmos[i])

    plt.xlabel('Nombre del archivo')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución de algoritmos de ordenamiento')
    plt.legend()
    plt.show()

# Ejemplo de uso
archivos = ['100', '500']
comparar_tiempos_algoritmos(archivos)
