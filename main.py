from PyQt5 import QtWidgets, QtCore
from ui import Ui_MainWindow
from creater import image_handler
import threading

def change():
    try:
        ui.buttonEnter.setEnabled(False)
        path = ui.textEdit.toPlainText()
        new_file = image_handler(path)
        if ui.radioNoise.isChecked():
            quantity_errors = int(ui.errors.toPlainText())
            new_file.image_with_errors(quantity_errors)
        if ui.radioEncode.isChecked():
            new_file.image_to_json()
        if ui.radioDecode.isChecked():
            new_file.image_to_jpg()
        ui.buttonEnter.setEnabled(True)
    except:
        ui.textEdit.setText('Choose a file')
    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.buttonEnter.clicked.connect(lambda: change())
    sys.exit(app.exec_())