import sys
import math
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt, QPointF, QPropertyAnimation, Property

class CircleLoadingWidget(QWidget):

    def __init__(
            self,
            loops: int = -1,
            pen_color: Qt = Qt.white,
            pen_width: int = 1,
            radius: int = 12,
            degrees: int = 360):

        super().__init__()

        self.loops = loops
        self.pen_color = pen_color
        self.pen_width = pen_width
        self.radius = radius

        if degrees < 0:
            raise ValueError("ERROR: degrees argument must be positive")
        
        if degrees > 360:
            raise ValueError("ERROR: degrees argument must be less than of equal to 360")
        
        self.degrees = degrees
        self._angle = 0

        self.animation = QPropertyAnimation(self, b"angle")
        self.animation.setStartValue(0)
        self.animation.setEndValue(360)
        self.animation.setDuration(2000)
        self.animation.setLoopCount(self.loops)
        self.animation.start()

    def paintEvent(self, event):
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(self.pen_color, self.pen_width)
        painter.setPen(pen)

        center_x = self.width() / 2
        center_y = self.height() / 2
        painter.translate(center_x, center_y)

        painter.rotate(self._angle)

        points = []

        for degree in range(self.degrees + 1):
            
            angle = math.radians(degree)
            
            x = self.radius * math.cos(angle)
            y = self.radius * math.sin(angle)
            
            points.append(QPointF(x, y))

        for index in range(len(points) - 1):
            painter.drawLine(points[index], points[index + 1])
    
    def get_angle(self):
        return self._angle
    
    def set_angle(self, value):
        self._angle = value
        self.update()
    
    angle = Property(float, get_angle, set_angle)

app = QApplication(sys.argv)

w = CircleLoadingWidget(
    degrees = 270,
    radius = 100
    )

w.show()
sys.exit(app.exec())