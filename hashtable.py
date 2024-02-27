class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key = "", data = None, next = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data
      self.next = next

    def __repr__(self):
        return str(self.data)

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = int(size)
        self.lista = [None] * self.size 

    def __repr__(self):
        return str(self.lista)
    
 
    def store(self, key, data=None):
        """key är nyckeln
            data är objektet som ska lagras
            om store anropas med bara en parameter så ska None lagras
            Stoppar in "data" med nyckeln "key" i tabellen."""
        ny_nod = HashNode(key, data)
        ny_hashning = self.hashfunction(key)
        gammal_nod = self.lista[ny_hashning]

        if gammal_nod is None:
            self.lista[ny_hashning] = ny_nod
        else:
            while gammal_nod.next is not None:
                if gammal_nod.key == key:
                    gammal_nod.data = ny_nod.data
                    break
                gammal_nod = gammal_nod.next

            if gammal_nod.key == key:
                gammal_nod.data = ny_nod.data
            else:
                gammal_nod.next = ny_nod
       
        


    def search(self, key):
        """key är nyckeln
            Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
            Om "key" inte finns ska det bli KeyError """
        index = self.hashfunction(key)
        nod = self.lista[index]
        while nod != None:
            if nod.key == key:
                return nod
        
            else:
                nod = nod.next
        raise KeyError


    def __contains__(self, key):
        """key är nyckeln
            Returnerar True om "key" finns i tabellen, annars False."""
        index = self.hashfunction(key)
        nod = self.lista[index]
        while nod != None:
            if nod.key == key:
                return True
            else:
                nod = nod.next
        return False



    def hashfunction(self, key):
        
        resultat = 0
        for k in key:
            resultat = (resultat*64 + ord(k))%self.size
        return resultat
    

 

        

        #samma hashning men olika keys










#hjälplista: testning del-1