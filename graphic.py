from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import os
import time

import cameraStream
import cv2

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        self.saveDir = ''
        self.saveDir_qle = QLineEdit()

        self.initUI()

        self.w = self.width() / 2
        self.h = self.height()

        self.cs = cameraStream.CameraStream(self)
        self.cs.changePixmap.connect(self.setImage)
        self.cs.start()

    def initUI(self):
        main_hbox = QHBoxLayout()

        stream_vbox = QHBoxLayout()
        input_vbox = QVBoxLayout()

        info_hbox = QHBoxLayout()

        fio_vbox = QVBoxLayout()

        self.s_lbl = QLabel('STREAM')
        stream_vbox.addStretch(1)
        stream_vbox.addWidget(self.s_lbl)

        surname_hbox = QHBoxLayout()
        surname_hbox.addStretch(1)
        surname_lbl = QLabel('Фамилия')
        self.surname_qle = QLineEdit()
        self.surname_qle.setFixedSize(300, 25)
        surname_hbox.addWidget(surname_lbl)
        surname_hbox.addWidget(self.surname_qle)

        name_hbox = QHBoxLayout()
        name_hbox.addStretch(1)
        name_lbl = QLabel('Имя')
        self.name_qle = QLineEdit()
        self.name_qle.setFixedSize(300, 25)
        name_hbox.addWidget(name_lbl)
        name_hbox.addWidget(self.name_qle)

        middleName_hbox = QHBoxLayout()
        middleName_hbox.addStretch(1)
        middleName_lbl = QLabel('Отчество')
        self.middleName_qle = QLineEdit()
        self.middleName_qle.setFixedSize(300, 25)
        middleName_hbox.addWidget(middleName_lbl)
        middleName_hbox.addWidget(self.middleName_qle)

        division_hbox = QHBoxLayout()
        division_hbox.addStretch(1)
        division_lbl = QLabel('Подразделение')
        self.division_qle = QLineEdit()
        self.division_qle.setFixedSize(300, 25)
        division_hbox.addWidget(division_lbl)
        division_hbox.addWidget(self.division_qle)

        fio_vbox.addLayout(surname_hbox)
        fio_vbox.addLayout(name_hbox)
        fio_vbox.addLayout(middleName_hbox)
        fio_vbox.addLayout(division_hbox)
        fio_vbox.addStretch(1)

        info_hbox.addStretch(1)
        info_hbox.addLayout(fio_vbox)
        info_hbox.addStretch(1)

        save_hbox = QHBoxLayout()
        save_hbox.addStretch(1)
        save_btn = QPushButton('СДЕЛАТЬ СНИМОК')
        save_btn.setFixedSize(400, 100)
        save_btn.clicked.connect(self.saveImage)
        save_hbox.addWidget(save_btn)
        save_hbox.addStretch(1)

        openDir_hbox = QHBoxLayout()
        openDir_hbox.addStretch(1)
        openDir_btn = QPushButton('Выбрать папку для сохранения')
        openDir_btn.clicked.connect(self.getDirectory)
        openDir_hbox.addWidget(openDir_btn)
        openDir_hbox.addWidget(self.saveDir_qle)
        openDir_hbox.addStretch(1)

        input_vbox.addLayout(info_hbox)
        input_vbox.addStretch(1)
        input_vbox.addLayout(save_hbox)
        input_vbox.addStretch(1)
        input_vbox.addLayout(openDir_hbox)

        main_hbox.addLayout(stream_vbox)
        main_hbox.addLayout(input_vbox)

        widget = QWidget()
        widget.setLayout(main_hbox)

        self.setWindowTitle('PhotkaemRoju')
        self.setGeometry(600, 300, 1000, 600)
        self.setCentralWidget(widget)
        self.show()

    def setImage(self, img):
        self.s_lbl.setPixmap(QPixmap(img).scaled(self.w, self.h))

    def getDirectory(self):
        dir = QFileDialog.getExistingDirectory(self, 'Выбрать папку', '.')
        self.saveDir = dir
        self.saveDir_qle.setText(self.saveDir)

    def saveImage(self):
        imageName = self.surname_qle.text() + self.name_qle.text() + self.middleName_qle.text() + self.division_qle.text()

        path = os.path.join(self.saveDir, imageName + '.png')
        self.s_lbl.pixmap().save(path)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()

    app.exec_()
