from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QComboBox, QAbstractItemView, QPushButton, QLabel, QLineEdit, QSpinBox, QHBoxLayout
from PyQt5.QtCore import QRect
import sys

data = {'Lunes':[' ',' ',' ',' ',' ',' ',' ',' '],
        'Martes':[' ',' ',' ',' ',' ',' ',' ',' '],
        'Miércoles':[' ',' ',' ',' ',' ',' ',' ',' '],
        'Jueves':[' ',' ',' ',' ',' ',' ',' ',' '],
        'Viernes':[' ',' ',' ',' ',' ',' ',' ',' ']}

class VentanaHorario(QWidget):
    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)
    
    def init_gui(self, tamano_ventana):
        self.setGeometry(tamano_ventana)
        self.setWindowTitle('Generador Horarios')
        self.contenedor = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setRowCount(10)
        columnas = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        self.table.setHorizontalHeaderLabels(columnas)
        self.table.move(0,0)
        self.selecciones = []
        self.modulos_a_repartir = 35
        self.valor_inicial = self.modulos_a_repartir
        # for col in range(self.table.columnCount()):
        #     for row in range(self.table.rowCount()):
        #         self.table.setItem()
        # self.table.show()
    
        self.contenedor.addWidget(self.table)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        
        self.btn = QPushButton("Fijar horario")
        self.btn.clicked.connect(self.fijar_horario)
        self.btn.setEnabled(False)
        self.contenedor.addWidget(self.btn)

        self.table.cellClicked.connect(self.click_forma_horario)
        self.table.cellEntered.connect(self.drag)
        self.table.cellPressed.connect(self.press)

        self.counter = QLabel(f'Módulos a repartir: {str(self.modulos_a_repartir)}')
        self.contenedor.addWidget(self.counter)

        self.setLayout(self.contenedor)

    def click_forma_horario(self, row, column):
        if (row, column) not in self.selecciones:
            self.selecciones.append((row, column))
            self.modulos_a_repartir -= 1
            self.counter.setText(f'Módulos a repartir: {str(self.modulos_a_repartir)}')
            if self.modulos_a_repartir == 0:
                self.btn.setEnabled(True)
            else:
                self.btn.setEnabled(False)
        else: 
            self.selecciones.remove((row, column))
            self.modulos_a_repartir += 1
            self.counter.setText(f'Módulos a repartir: {str(self.modulos_a_repartir)}')
            if self.modulos_a_repartir == 0:
                self.btn.setEnabled(True)
            else:
                self.btn.setEnabled(False)

    def press(self, row, column):
        self.ultima_tupla = (row, column)
        if (row, column) in self.selecciones:
            self.activa = False
        else:
            self.activa = True
        
    def drag(self, row, column):
        if self.activa:
            if self.ultima_tupla[0] < row:
                limite_inferior_row = self.ultima_tupla[0]
                limite_superior_row = row + 1
            else:
                limite_inferior_row = row
                limite_superior_row = self.ultima_tupla[0] + 1
            if self.ultima_tupla[1] < column:
                limite_inferior_column = self.ultima_tupla[1]
                limite_superior_column = column + 1
            else:
                limite_inferior_column = column
                limite_superior_column = self.ultima_tupla[1] + 1
             
            for r in range(limite_inferior_row, limite_superior_row):
                for c in range(limite_inferior_column, limite_superior_column):
                    if (r, c) not in self.selecciones:
                        self.selecciones.append((r, c))
                        self.modulos_a_repartir -= 1
                        self.counter.setText(f'Módulos a repartir: {str(self.modulos_a_repartir)}')
                        if self.modulos_a_repartir == 0:
                            self.btn.setEnabled(True)
                        else:
                            self.btn.setEnabled(False)

        else:
            for r in range(self.ultima_tupla[0], row + 1):
                for c in range(self.ultima_tupla[1], column + 1):
                    if (r, c) in self.selecciones:
                        self.selecciones.remove((r,c))
                        self.modulos_a_repartir += 1
                        self.counter.setText(f'Módulos a repartir: {str(self.modulos_a_repartir)}')
                        if self.modulos_a_repartir == 0:
                            self.btn.setEnabled(True)
                        else:
                            self.btn.setEnabled(False)            

    def fijar_horario(self):
        self.cbs = []
        for i in range(len(self.selecciones)):
            self.cbs.append(QComboBox())
            self.cbs[i].addItem('')
            self.cbs[i].addItem('Matemáticas')
            self.cbs[i].addItem('Lenguaje')
            self.table.setCellWidget(self.selecciones[i][0], self.selecciones[i][1], self.cbs[i])

class CantidadModulos(QWidget):
    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):
        self.setGeometry(tamano_ventana)
        self.setWindowTitle('Generador Horarios')

        self.contenedor = QVBoxLayout()

        self.vbox = QVBoxLayout()
        self.boton = QVBoxLayout()
        
        self.lista_hboxs = []
        self.lista_infos = []

        hbox = QHBoxLayout()
        self.lista_hboxs.append(hbox)

        nombre_ramo = QLineEdit()

        nombre_profesor = QComboBox()
        nombre_profesor.addItems([])
        nombre_profesor.setEditable(True)

        cantidad_horas = QSpinBox()

        self.boton = QPushButton('+')

        self.boton.clicked.connect(self.agregar_otro_ramo)

        self.lista_infos.append((nombre_ramo,nombre_profesor,cantidad_horas))

        hbox.addWidget(nombre_ramo)
        hbox.addWidget(nombre_profesor)
        hbox.addWidget(cantidad_horas)

        self.vbox.addLayout(hbox)

        self.contenedor.addLayout(self.vbox)

        self.contenedor.addWidget(self.boton)

        self.setLayout(self.contenedor)


    def agregar_otro_ramo(self):
        hbox = QHBoxLayout()

        nombre_ramo = QLineEdit()
        nombre_profesor = QComboBox()
        nombre_profesor.addItems([])
        nombre_profesor.setEditable(True)

        cantidad_horas = QSpinBox()

        hbox.addWidget(nombre_ramo)
        hbox.addWidget(nombre_profesor)
        hbox.addWidget(cantidad_horas)

        self.vbox.addLayout(hbox)




def main(args):
    app = QApplication(args)
    dims = (100, 100, 1200, 900)
    container = VentanaHorario(QRect(*dims))
    # container = CantidadModulos(QRect(*dims))
    # table = TableView(data, 9, 5)
    container.show()
    # container.addWidget(table)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv)