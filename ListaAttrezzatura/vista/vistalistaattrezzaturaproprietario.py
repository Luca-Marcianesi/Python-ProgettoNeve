from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy, QListView, QPushButton, QDesktopWidget, QMessageBox

from Attrezzatura.vista.VistaAttrezzaturaProprietario import VistaAttrezzaturaProprietario
from ListaAttrezzatura.controller.controllerlistaattrezzatura import ControllerListaAttrezzatura
from Attrezzatura.vista.VistaAggiungiAttrezzatura import VistaAggiungiAttrezzatura

# Vista lista attrezzatura proprietario


class VistaListaAttrezzaturaProprietario(QWidget):
    def __init__(self, callback):
        super(VistaListaAttrezzaturaProprietario, self).__init__()

        # Attributi
        self.controller_lista_attrezzatura = ControllerListaAttrezzatura()
        self.callback = callback
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Sfondo
        self.show_background("LISTA ATTREZZATURA")

        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200))

        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))

        # Lista
        self.vista_lista = QListView()

        label = self.aggiorna()

        self.layout_orizzontale.addWidget(label)

        self.layout_orizzontale.addSpacerItem(QSpacerItem(1000, 0))

        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        if self.controller_lista_attrezzatura.get_lista_filtrata() == []:
            self.layout_verticale1.addSpacerItem(QSpacerItem(0, 350))
        else:
            self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Lista Attrezzatura')

    # Metodo che, collegato al pulsante "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.controller_lista_attrezzatura.salva_dati()
        self.close()

    # Creazione, settaggio e stile dello sfondo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ListaAttrezzatura/data/ListaAttrezzatura.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Creazione, settaggio e stile dei pulsanti
    def show_pulsantiera(self):
        if not self.controller_lista_attrezzatura.get_lista_filtrata() == []:
            pulsante_apri = self.pulsante("Apri", self.attrezzatura_selezionata)
            pulsante_apri.clicked.connect(self.attrezzatura_selezionata)
            self.layout_verticale2.addWidget(pulsante_apri)

        # Pulsante aggiungi
        pulsante_aggiungi = self.pulsante("Aggiungi\nattreazzatura", self.aggiungi)
        self.layout_verticale2.addWidget(pulsante_aggiungi)

        # Pulsante indietro
        pulsante_indietro = self.pulsante("Indietro", self.indietro)
        self.layout_verticale2.addWidget(pulsante_indietro)

        self.layout_orizzontale.addLayout(self.layout_verticale2)

    # Metodo che aggiorna la finestra
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.vista_lista)
        if self.controller_lista_attrezzatura.get_lista_attrezzatura() == []:
            label = QLabel(" Non ci sono oggetti disponibili")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont('Times New Roman', 25, 100))
            label.setStyleSheet('QLabel {background-color: lightBlue; color: black;}')
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            self.layout_orizzontale.addSpacerItem(QSpacerItem(0, 50))
            return label
        else:
            for attrezzatura in self.controller_lista_attrezzatura.get_lista_attrezzatura():
                item = QStandardItem()
                nome = attrezzatura.get_nome()
                if attrezzatura.get_stato():
                    item.setForeground(QColor(0, 255, 0))
                else:
                    item.setForeground(QColor(255, 0, 0))
                item.setText(nome)
                item.setEditable(False)
                item.setFont(QFont('Times New Roman', 30, 100))
                vista_lista_model.appendRow(item)
            self.vista_lista.setModel(vista_lista_model)
            return self.vista_lista

    # Metodo che gestisce la situazione in cui al click del pulsante "APRI", non venga selezionato niente

    def attrezzatura_selezionata(self):
        try:
            selezionata = self.vista_lista.selectedIndexes()[0].row()
            lista = self.controller_lista_attrezzatura.get_lista_attrezzatura()
            attrezzatura = lista[selezionata]
            self.vista_attrezzatura = VistaAttrezzaturaProprietario(
                self.showFullScreen, attrezzatura, self.controller_lista_attrezzatura.rimuovi_attrezzatura,
                self.aggiorna)
            self.vista_attrezzatura.showFullScreen()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessuna attrezzatura.', QMessageBox.Ok,
                                    QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.', QMessageBox.Ok,
                                 QMessageBox.Ok)

    # Crea un pulsante

    def pulsante(self, nome, call):
        pulsante = QPushButton(nome)
        pulsante.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante.setFixedSize(250, 100)
        pulsante.clicked.connect(call)
        return pulsante

    def aggiungi(self):
        self.vista_aggiungi_attrezzatura = VistaAggiungiAttrezzatura(
            self.showFullScreen, self.controller_lista_attrezzatura, self.aggiorna)
        self.vista_aggiungi_attrezzatura.show()