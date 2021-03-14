from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage


import cv2


class CameraStream(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        cap = cv2.VideoCapture(cv2.CAP_DSHOW, 0)

        while True:
            ret, source_img = cap.read()

            if ret:
                img = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)
                height, width, channel = img.shape
                step = channel * width
                qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
                self.changePixmap.emit(qImg)

            cv2.waitKey(1)
