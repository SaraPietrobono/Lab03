from logging import exception
from auto import Automobile
import csv
class Noleggio:
    def __init__(self,codice,data,id_automobile,cognome_cliente):
        self.codice=codice
        self.data=data
        self.id_automobile=id_automobile
        self.cognome_cliente=cognome_cliente
    def __str__(self):
        return f'Noleggio {self.codice}- Auto {self.id_automobile}- Cliente{self.cognome_cliente}-Data{self.data}'

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.responsabile=responsabile
        self.automobile=[]
        self.noleggi=[]

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            with open(file_path, 'r',encoding='utf-8') as f:
                reader=csv.reader(f)
                for riga in reader:
                    if len(riga)<5:
                        continue
                    codice,marca,modello,anno,posti=riga
                    auto=Automobile(codice,marca,modello,anno,posti)
                    self.automobile.append(auto)  #abbiamo creato una lista di classi (ogni classe è un automobile)
        except FileNotFoundError:
            return FileNotFoundError('File not found')
    def aggiungi_automobile(self, marca, modello, anno, posti):
        for auto in self.automobile:
            if (auto.marca.lower()==marca.lower() and  auto.modello.lower() == modello.lower() and auto.anno == int(anno) and auto.posti ==int(posti)):
                raise Exception('Errore: Automobile già presente nel sistema')
        if len(self.automobile)==0:
            nuovo_cod='A1'
        else:
            ultimo_cod=self.automobile[-1].codice #in questo modo mi prendo il codice dell'ultima auto
            cod=int(ultimo_cod[1:])+1 #prendo in considerazione solo la parte numerica del codice (senza la lettera A davanti) e lo incremento di 1
            nuovo_cod=f'A{cod}'
        auto=Automobile(nuovo_cod,marca,modello,int(anno),int(posti))
        self.automobile.append(auto)
        return auto
    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO
        return sorted(self.automobile, key=lambda x: x.marca.lower() )
    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO
        #verifico che l'auto sia presente nel sistema
        auto_richiesta=None
        for auto in self.automobile:
            if auto.codice==id_automobile:
                auto_richiesta=auto
                break
        #se l'auto non è stato trovata si solleva un eccezzione
        if auto_richiesta is None:
            raise Exception('Errore: Auto non trovata')
        if auto_richiesta.noleggiata:
            raise Exception('Errore: Auto noleggiata')
        if len(self.noleggi)==0:
            new_cod='N1' #se non sono presenti macchine noleggiate si inizializza la prima con il primo codice
        else:
            last_cod=self.noleggi[-1].codice
            codd=int(last_cod[1:])+1
            new_cod=f'N{codd}'

        noleggio_nuovo=Noleggio(new_cod,data,id_automobile,cognome_cliente)
        auto_richiesta.noleggiata=True
        self.noleggi.append(noleggio_nuovo)
        return noleggio_nuovo
    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
        noleggio_richiesto=None
        for n in self.noleggi:
            if n.codice==id_noleggio:
                noleggio_richiesto=n
                break
        if noleggio_richiesto is None:
            raise Exception('Errore: noleggio non trovato')
        auto_richiesta=None
        for auto in self.automobile:
            if auto.codice==noleggio_richiesto.id_automobile:
                auto_richiesta=auto
        if auto_richiesta is not None:
            auto_richiesta.noleggiata=False
        self.noleggi.remove(noleggio_richiesto)
        print(f'Noleggio {id_noleggio} terminato ')
