class sessione:

    account_loggato = None

    @classmethod
    def login(cls,account):
        cls.account_loggato = account

    @classmethod
    def cambia_eta(cls,eta):
        cls.account_loggato.set_eta(eta)

    @classmethod
    def cambia_numero_scarpe(cls, numero_scarpe):
        cls.account_loggato.set_numero_scarpe(numero_scarpe)

    @classmethod
    def cambia_altezza(cls, altezza):
        cls.account_loggato.set_altezza(altezza)

    @classmethod
    def cambia_password(cls, password):
        cls.account_loggato.set_password(password)

    @classmethod
    def aggiungi_prenotazione(cls,prenotazione):
        cls.account_loggato.aggiungi_prenotazione(prenotazione)

    @classmethod
    def cancella_prenotazione(cls):
        cls.account_loggato.rimuovi_prenotazione()

    @classmethod
    def get_lista_prenotazioni(cls):
        return cls.account_loggato.get_lista_prenotazioni()

    @classmethod
    def get_nome(cls):
         return cls.account_loggato.get_nome()

    @classmethod
    def get_cognome(cls):
        return cls.account_loggato.get_cognome()

    @classmethod
    def get_eta(cls):
        return cls.account_loggato.get_eta()

    @classmethod
    def get_numero_scarpe(cls):
        return cls.account_loggato.get_numero_scarpe()

    @classmethod
    def get_altezza(cls):
        return cls.account_loggato.get_altezza()
