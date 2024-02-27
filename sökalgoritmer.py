from del1Labb6 import *
from heapsort import *




def linear_search(arr, target = None):
    """
    Linjärsökning (linear search) är en enkel sökalgoritm som går igenom varje element i en lista
    och jämför det med målet. Om målet hittas returneras dess index, annars returneras -1.
    """
    for i in range(len(arr)):
        if arr[i].artistnamn == target:
            return arr[i]
    return f'{target} hittades inte i listan.'

def binary_search(arr, target):
    """
    Binärsökning (binary search) är en effektiv sökalgoritm som används på sorterade listor.
    Algoritmen jämför målet med mitten av listan och eliminerar hälften av listan vid varje steg.
    Om målet hittas returneras dess index, annars returneras -1.
    """
    target = Song(artistnamn = target)
    low = 0
    high = len(arr) - 1

    while low <= high: # så länge low är mindre än eller lika med high
        mid = (low + high) // 2
        if arr[mid].artistnamn == target.artistnamn: # om arr[mid] är lika med target
            return mid
        elif arr[mid].artistnamn < target.artistnamn: 
            low = mid + 1 # om arr[mid] är mindre än target, öka low
        else:
            high = mid - 1 # om arr[mid] är större än target, minska high

    return f'{target} hittades inte i listan.'
