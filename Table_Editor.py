import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QAbstractTableModel

class TableModel(QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data
        self.header = header

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[section]
        return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set window title and size
        self.setWindowTitle("Information Table")
        self.setGeometry(100, 100, 800, 600)

        # Create table data
        data = []
        for i in range(20):
            row = ["", "", "", "", "", "", "", ""]
            data.append(row)

        # Set table header
        header = ["Wallets", "Discord", "Twitter", "Email", "Balance", "Lock", "Source Exchange", "Addinfo"]

        # Create table model
        model = TableModel(data, header)

        # Create table view
        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QTableView.Stretch)
        table_view.verticalHeader().setSectionResizeMode(QTableView.Stretch)

        # Set main layout
        layout = QVBoxLayout()
        layout.addWidget(table_view)

        # Create central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set central widget
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
