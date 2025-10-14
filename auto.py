class Automobile:
    def __init__(self,codice,marca,modello,anno, posti):
        self.codice = codice
        self.marca=marca
        self.modello=modello
        self.anno=int(anno)
        self.posti=int(posti)
        self.noleggiata=False #è lo stato in cui si trova la macchina

    def __str__(self):
        if self.noleggiata==False:
            stato='Disponibile'
        else:
            stato='Noleggiata'
        return f'codice: {self.codice}, marca: {self.marca}, modello: {self.modello}, anno di immatricolazione: {self.anno}, posti:{self.posti}, stato: {stato}'

