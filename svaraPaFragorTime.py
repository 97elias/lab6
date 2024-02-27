'''
Parametern "stmt" representerar den kod som ska mätas i tid. 
Det kan vara en enkel kodrad eller en kodblock som ska utföras upprepade gånger.


Parametern "number" representerar antalet gånger som koden i "stmt" 
ska köras för att mäta tiden. Ju högre värde för "number", 
desto mer exakt blir tidsmätningen.

Funktionen "timeit" mäter tiden det tar att köra koden i "stmt" ett visst antal gånger,
enligt värdet på "number". Den används för att mäta prestanda
och jämföra olika implementationer av kod.


Ett anrop av "timeit" returnerar en mätning av den totala tiden det tog att
köra koden i "stmt" det angivna antalet gånger. Det kan vara en flyttalsvärde
som representerar antalet sekunder det tog att köra koden.

 '''