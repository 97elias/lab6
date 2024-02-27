class Song:
    def __init__(self, trackid = None, låttid= None, artistnamn= None, låttitel= None,):
        self.trackid = trackid
        self.låttid = låttid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __repr__(self):
        return f'Artist: {self.artistnamn} Låt: {self.låttitel}\n'
    
    def __lt__(self, other):
        if self.artistnamn == other.artistnamn:
            return self.låttitel < other.låttitel
        else:
            return self.artistnamn < other.artistnamn

def låtar_indexlista():
    with open("unique_tracks.txt", "r", encoding = "utf-8") as låttexter:
        låtlista = []
        for rad in låttexter:
            delrad = rad.strip().split('<SEP>')
 
            låtlista.append(Song(*delrad))
    return låtlista

def låtar_dict():
    låtar = {}
    with open("unique_tracks.txt", "r", encoding = "utf-8") as låttexter:
        for rad in låttexter:
            delrad = rad.strip().split('<SEP>')

            dict_obj = Song(*delrad)
            if dict_obj.artistnamn in låtar:
                låtar[dict_obj.artistnamn].append(dict_obj)
            else:
                låtar[dict_obj.artistnamn] = [dict_obj]
    return låtar


