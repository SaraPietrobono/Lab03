from auto import Automobile
import csv
class Autonoleggio:
    def __init__(self, nome, responsabile,automobile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.responsabile=responsabile
        self.automobile=[]

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            with open(file_path, 'r',encoding='utf-8') as f:
                for line in f:
                    campi=line.strip('').split('')
                    codice=campi[0]
                    marca=campi[1]
                    modello=campi[2]
                    anno=campi[3]
                    posti=campi[4]
                    C=Automobile(codice,marca,modello,anno,posti)
                    self.automobile.append(C)
        except FileNotFoundError:
            return None
    def aggiungi_automobile(self, marca, modello, anno, num_posti, automobile):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO



    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
