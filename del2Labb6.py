from heapsort import *
def main():
    songs = readFile()
    print(pickOut(songs[:11], 1))
    
     
    #print(linearSearch(songs, 1))


class SongK():
    def __init__(self, artisttid = None, artistnamn = None, sångtitel = None, 
                    låtlängd = None, år = None):
        self.artisttid = artisttid
        self.artistnamn = artistnamn
        self.sångtitel = sångtitel
        self.låtlängd = låtlängd
        self.år = år

    def __repr__(self):
        return f'Artist: {self.artistnamn}. Låt: {self.sångtitel}. Låtlängd: {self.låtlängd}sekunder. År: {self.år}\n'
    
    def __lt__(self, other):
        return self.låtlängd < other.låtlängd
    
    def __eq__(self, other):
        return self.låtlängd == other.låtlängd
    
def pickOut(lista, k):
    
    sortedList = heapsort(lista)
    print(sortedList)
    indexK = sortedList[len(sortedList)-k]
    
    return indexK

def linearSearch(lista, k):
    
    currentIndex = 0
    for i in range(k):
        for j in range(len(lista)):
            if float(lista[j].låtlängd) > float(lista[currentIndex].låtlängd):
                currentIndex = j
                
        longestSong = lista.pop(currentIndex)
       
    return longestSong


def readFile(): #läs in filen med nya låtar
    #input: ingen
    #output: en lista med objekt av klassen SongK
    songs = []
    with open("låtar_ny.txt", "r", encoding = "utf-8") as file: #öppna filen
        lines = file.readlines() #läs in filen
        for line in lines: #för varje rad i filen
            attributes = line.strip().split("\t") #splitta raden
            song = SongK(*attributes) #skapa ett objekt med attributen
            songs.append(song)
    return songs


main()