import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
from PIL.ImageQt import ImageQt

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui_file_path = os.path.join(os.path.dirname(__file__), "MainWindow.ui")
        uic.loadUi(ui_file_path, self)


        self.image_frame = self.findChild(QtWidgets.QLabel, 'image_frame')

        self.edit_horizontalSlider = self.findChild(QtWidgets.QSlider, 'edit_horizontalSlider')
        self.edit_horizontalSlider.valueChanged.connect(self.changeValue)


        self.edit_label = self.findChild(QtWidgets.QLabel, 'edit_label')

        image = Image.open('/home/pedro/Downloads/pinguin.png')
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")

        qim = QImage(data, image.size[0], image.size[1], QImage.Format_ARGB32)

        pixmap = QPixmap.fromImage(qim)
        self.image_frame.setPixmap(pixmap)
        self.show()

    def change_edit_label(self, value):
        self.edit_label.setText(value)

    def changeValue(self, value):
        self.change_edit_label(str(value))