from ElencoManutenzioni.model.elenco_manutenzioni import elenco_manutenzioni

class controller_elenco_manutenzioni():

    def __init__(self):
        self.model = elenco_manutenzioni()

    def salva_dati(self):
        self.model.salva_dati()