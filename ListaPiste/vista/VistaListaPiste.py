from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QPushButton, \
    QDesktopWidget
from ListaPiste.controller.controller_lista_piste import controller_lista_piste


class vista_piste(QWidget):
    def __init__(self, callback):
        super(vista_piste, self).__init__()

        # Attributi
        self.controller = controller_lista_piste()
        self.callback = callback
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Sfondo
        self.show_background("LISTA PISTE")

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Lista
        vista_lista = QListView()
        vista_lista_model = QStandardItemModel(vista_lista)
        for pista in self.controller.get_lista():
            item = QStandardItem()
            item.setText(pista.get_nome_str())
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 16))
            vista_lista_model.appendRow(item)
        vista_lista.setModel(vista_lista_model)
        self.layout_orizzontale.addWidget(vista_lista)

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Lista Piste')

    def closeEvent(self, event):
        pass

    def call_vista_pista(self):
        pass

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

    def show_pulsantiera(self):
        # Punsante apri
        layout_pulsanti = QVBoxLayout()
        pulstante_apri = QPushButton("APRI")
        pulstante_apri.setFont(QFont('Times New Roman', 18))
        pulstante_apri.setFixedSize(250, 100)
        pulstante_apri.clicked.connect(self.call_vista_pista)
        layout_pulsanti.addWidget(pulstante_apri)
        layout_pulsanti.addStretch()

        # Punsante indietro
        pulstante_indietro = QPushButton("INDIETRO")
        pulstante_indietro.setFont(QFont('Times New Roman', 18))
        pulstante_indietro.setFixedSize(250, 100)
        pulstante_indietro.clicked.connect(self.indietro)
        layout_pulsanti.addWidget(pulstante_indietro)
        layout_pulsanti.addStretch()
        layout_pulsanti.addSpacerItem(QSpacerItem(0, 500, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addLayout(layout_pulsanti)