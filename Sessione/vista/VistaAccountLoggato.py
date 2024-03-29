from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QDesktopWidget, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import Qt
from Sessione.controller.controllersessione import ControllerSessione
from Sessione.vista.VistaModificaAccount import VistaModificaAccount

from Sessione.vista.VistaPrenotazioneAccount import VistaPrenotazioneAccount

# Vista account loggato
class VistaAccountLoggato(QWidget):

    def __init__(self, callback):
        super(VistaAccountLoggato, self).__init__()

        # Controller relativo alla vista
        self.controller = ControllerSessione()

        # Layout utilizzati dalla vista per l'allineamento dei widget
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale3 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Label che illustra le informazioni utili
        self.label = QLabel()

        # Viste successive
        self.vista_modifica_credenziali = VistaModificaAccount(self.aggiorna, self.showFullScreen)
        self.vista_prenotazione_account = VistaPrenotazioneAccount(self.showFullScreen)

        # vista precedente
        self.callback = callback

        # Impostazione dello sfondo e del titolo
        self.show_background("INFORMAZIONI ACCOUNT")

        # Spaziatura
        self.layout_verticale3.addSpacerItem(QSpacerItem(0, 60))

        # Chiamata alla funzione aggiorna
        self.aggiorna()

        # Aggiunta della label al layout
        self.layout_verticale3.addWidget(self.label)

        # Spaziatura
        self.layout_verticale3.addSpacerItem(QSpacerItem(0, 500))
        self.layout_orizzontale.addLayout(self.layout_verticale3)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(700, 0))

        # Pulsanti cambia credenziali, prenotazioni e indietro + allineamento
        self.show_pulsantiera()

        # Spaziatura e allineamento
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200))

        # Settaggio layout
        self.setLayout(self.layout_verticale1)

    # Creazione, settaggio e stile pulsanti
    def show_pulsantiera(self):

        # Cambia Credenziali
        pulsante_credenziali = self.crea_bottone("CAMBIA\nCREDENZIALI", self.layout_verticale2)
        pulsante_credenziali.clicked.connect(self.call_modifica_credenziali)

        if self.controller.get_permessi() is False:
            pulsante_prenotazioni = self.crea_bottone("PRENOTAZIONI", self.layout_verticale2)
            pulsante_prenotazioni.clicked.connect(self.vista_prenotazioni)

        pulsante_indietro = self.crea_bottone("INDIETRO", self.layout_verticale2)
        pulsante_indietro.clicked.connect(self.indietro)

        self.layout_orizzontale.addLayout(self.layout_verticale2)

    # Metodo che, collegato al bottone "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Metodo che richiama e mostra la vista modifica credenziali
    def call_modifica_credenziali(self):
        self.vista_modifica_credenziali.showFullScreen()
        self.close()

    # Metodo che richiama e mostra la vista prenotazioni
    def vista_prenotazioni(self):
        self.vista_prenotazione_account.showFullScreen()
        self.close()

    # Funzione standard per il settaggio dello sfondo e del titolo alla finestra
    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaSkipass.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60, 100))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        titolo.setStyleSheet('QLabel {color: black}')
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Metodo che aggiorna la finestra corrente
    def aggiorna(self):
        # Label
        self.label.setText("Nome: {}".format(self.controller.get_nome_str()) + "\n"
                           "Cognome: {}".format(self.controller.get_cognome_str()) + "\n"
                           "Età: {}".format(self.controller.get_eta_str()) + "\n"
                           "Altezza: {}".format(self.controller.get_altezza_str()) + "\n"
                           "Numero di scarpe: {}".format(self.controller.get_numero_scarpe_str()))
        self.label.setFont(QFont('Times New Roman', 30, 100))

    # Metodo che crea un generico bottone
    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(300, 100)
        bottone.setFont(QFont('Times New Roman', 20, 100, True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        layout.addWidget(bottone)
        return bottone
