import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor, QPen

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn_draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        qp.setPen(color)
        qp.setBrush(color)
        x = random.randint(10, 550)
        y = random.randint(50, 500)
        w = random.randint(10, 100)
        qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())