from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout, QSizePolicy, \
    QSpacerItem, QDesktopWidget
from PyQt5.QtCore import Qt

from Sessione.controller.controller_sessione import controller_sessione


class vista_modifica_account(QWidget):

    def __init__(self, callback):
        super(vista_modifica_account, self).__init__()

        # Attributi
        self.callback = callback
        self.controller = controller_sessione()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()
        self.testo = {}

        # Sfondo
        self.show_background("MODIFICA LE CREDENZIALI")

        # Spaziatura
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Caselle di testo allineate
        self.casella_testo("PASSWORD")
        self.casella_testo("ETÀ")
        self.casella_testo("ALTEZZA")
        self.casella_testo("NUMERO DI SCARPE")

        # Spaziatura
        self.layout_orizzontale2.addLayout(self.layout_verticale2)
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Pulsanti Indietro e Invia
        self.show_pulsatiera()

        # Impostazione layout
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle("Cambia Credenziali")

    def show_pulsatiera(self):
        # Indietro
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 17))
        pulsante_indietro.setFixedSize(200, 70)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale1.addWidget(pulsante_indietro)

        # Invio
        pulsante_invio = QPushButton("INVIA")
        pulsante_invio.setFont(QFont('Times New Roman', 17))
        pulsante_invio.setFixedSize(200, 70)
        pulsante_invio.clicked.connect(self.cambia_dati)
        self.layout_orizzontale1.addWidget(pulsante_invio)

        self.layout_verticale2.addLayout(self.layout_orizzontale1)
        self.layout_verticale1.addLayout(self.layout_orizzontale2)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Expanding, QSizePolicy.Expanding))

    def casella_testo(self, tipo):
        # Label
        label = QLabel(tipo + ":")
        label.setFont(QFont('Times New Roman', 30))
        label.setAlignment(Qt.AlignCenter)
        self.layout_verticale2.addWidget(label)

        #Casella di testo
        casella = QLineEdit()
        font = casella.font()
        font.setPointSize(15)
        casella.setFont(font)
        casella.setAlignment(Qt.AlignCenter)
        self.layout_verticale2.addWidget(casella)
        self.testo[tipo] = casella

    def cambia_dati(self):
        password = self.testo["PASSWORD"].text()
        eta = self.testo["ETÀ"].text()
        altezza = self.testo["ALTEZZA"].text()
        numero_scarpe = self.testo["NUMERO DI SCARPE"].text()
        if password != "" and eta != "" and altezza != "" and numero_scarpe != "":
            self.controller.cambia_password(password)
            self.controller.cambia_eta(eta)
            self.controller.cambia_altezza(altezza)
            self.controller.cambia_numero_scarpe(numero_scarpe)
            self.callback()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)

    def indietro(self):
        self.callback()
        self.close()


    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ListaAccount/data/im.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))