import sys
from random import choices

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class Yellow_rounds(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.btn_paint.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.begin(self)
            self.draw_round(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_round(self, qp):
        qp.setPen(QColor(255, 255, 0))
        a, b = choices(range(1, 200), k=2)
        qp.drawEllipse(a, a, b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow_rounds()
    ex.show()
    sys.exit(app.exec_())