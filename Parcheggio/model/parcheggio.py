from datetime import datetime
class parcheggio:
    def __init__(self, codice, numero, stato,):
        self.codice = codice
        self.numero = numero
        self.stato = stato
        self.scadenza = None

    def get_codice(self):
        return self.codice

    def get_scadenza(self):
        return self.scadenza

    def set_scadenza(self,scadenza):
        self.scadenza = scadenza

    def set_stato(self, stato):
        self.stato = stato

    def get_stato(self):
        return self.stato

    def prenota(self,scadenza):
        self.scadenza = scadenza
        self.set_stato(False)

    def elimina_prenotazione(self):
        self.scadenza = None
        self.set_stato(True)

    def get_numero(self):
        return self.numero

    def get_descrizione(self):
        return "Parcheggio numero {}".format(self.numero)
