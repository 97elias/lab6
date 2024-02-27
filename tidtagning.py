from del1Labb6 import *
from heapsort import *
from sökalgoritmer import *
from hashtable import *
from IndexlistQFile import *
from LinkedListQFile import *
from bintreeFile import *
import timeit, random

def main():
    # Test case
    låtar = låtar_indexlista()
    #låtarSorterad = heapsort(låtar) # sorterad lista


    #measurePartOne(låtar) 
    #measurePartOne(låtarSorterad)
    #measurePartTwo(låtar)
    
    # # III. ska kallas 1000ggr och ta genomsnittet av tiden
    # tidEtt = 0
    # tidTvå = 0
    # tidTre = 0
    # for i in range(1000):
    #     tid = measurePartTwo(låtarSorterad)
    #     tidEtt += tid[0]
    #     tidTvå += tid[1]
    #     tidTre += tid[2]
    # print(f'250k: {tidEtt/1000}\n500k: {tidTvå/1000}\n1000k: {tidTre/1000}')


    measurePartSeven(låtar)
    #measurePartOne(låtar)
    #measurePartOne(låtarSorterad)
    #measurePartTwo(låtarSorterad)


# här kan vi lägga in både en osorterad och sorterad lista (I & II)
def measurePartOne(lista):
    sampleSize = [250000, 500000, 1000000]
    for i in range(len(sampleSize)):
        listaNy = lista[:sampleSize[i]]
        target = lista[len(listaNy) - 2].artistnamn
        execution_time = timeit.timeit(lambda: linear_search(listaNy, target), number=5)
        print(f'Test: {sampleSize[i]}, Execution time: {execution_time:.3f} seconds')
        # Time complexity: O(n)


# (III)
def measurePartTwo(lista):
    sampleSize = [250000, 500000, 1000000]
    output = []
    for i in range(len(sampleSize)):
        listaNy = lista[:sampleSize[i]]
        target = random.choice(listaNy).artistnamn
        execution_time = timeit.timeit(lambda: linear_search(listaNy, target), number=5)
        output.append(execution_time)
    return output


# (IV) 
def measurePartThree(lista):
    sampleSize = [250000, 500000, 1000000]
    for i in range(len(sampleSize)):
        listaNy = lista[:sampleSize[i]]
        execution_time = timeit.timeit(lambda: heapsort(listaNy), number=5)
        print(f'Test i: {sampleSize[i]}, Execution time: {execution_time:.3f} seconds')
        # Time complexity: O(log n)


# (V) binärsökning i sorterad indexlista
def measurePartFour(listaSorterad):
    sampleSize = [250000, 500000, 1000000]
    for i in range(len(sampleSize)):
        listaNy = listaSorterad[:sampleSize[i]]
        target = random.choice(listaSorterad).artistnamn
        execution_time = timeit.timeit(lambda: binary_search(listaNy, target), number=5)
        print(f'Test i: {sampleSize[i]}, Execution time: {execution_time:.6f} seconds')
        # Time complexity: O(log n)


# (VI&VII) input: lista, kö(antingen länkad eller index)
def measurePartFive(lista, kö):
    sampleSize = [250000, 500000, 1000000]
    for size in sampleSize:
        listaNy = lista[:size]
        startTime = timeit.default_timer()
        for i in range(len(listaNy)):
            kö.enqueue(listaNy[i])
        for j in range(len(listaNy)):
            kö.dequeue()
        endTime = timeit.default_timer()
        execution_time = endTime - startTime
        print(f'Test {size}:, Execution time: {execution_time:.6f} seconds')


# (VIII) Lägg in n element i ett binärträd
def measurePartSix(lista):
    träd = Bintree()
    sampleSize = [250000, 500000, 1000000]
    for size in sampleSize:
        listaNy = lista[:size]
        startTime = timeit.default_timer()
        for i in range(len(listaNy)):
            träd.store(listaNy[i])
        endTime = timeit.default_timer()
        execution_time = endTime - startTime
        print(f'Test {size}:, Execution time: {execution_time:.6f} seconds')

# (IX) Lägg in n element i en Hashtabell
def measurePartSeven(lista):
    hash = Hashtable(1000000)
    sampleSize = [250000, 500000, 1000000]
    for size in sampleSize:
        listaNy = lista[:size]
        startTime = timeit.default_timer()
        for i in range(len(listaNy)):
            hash.store(listaNy[i].trackid, listaNy[i])
        endTime = timeit.default_timer()
        execution_time = endTime - startTime
        print(f'Test {size}, Execution time: {execution_time:.6f} seconds')


main()