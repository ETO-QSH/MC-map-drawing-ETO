from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QMovie
import sys

class AnimatedButton(QWidget):
    def __init__(self, on_gif_path, off_gif_path):
        super().__init__()

        self.current_state = "on"

        self.on_gif_path = on_gif_path
        self.off_gif_path = off_gif_path

        self.pixmap_on = QPixmap(self.on_gif_path)
        self.pixmap_off = QPixmap(self.off_gif_path)

        self.movie_on = QMovie(self.on_gif_path)
        self.movie_off = QMovie(self.off_gif_path)

        self.movie_on.setSpeed(1000)
        self.movie_off.setSpeed(1000)

        self.setFixedSize(self.pixmap_on.size())

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap_on)

        self.movie_on.frameChanged.connect(self.handle_frame_change)
        self.movie_off.frameChanged.connect(self.handle_frame_change)

        self.movie_on.jumpToFrame(0)
        self.movie_off.jumpToFrame(0)

    def handle_frame_change(self):
        if self.current_state == "transition":
            if self.movie_on.currentFrameNumber() == self.movie_on.frameCount() - 1:
                self.current_state = "off"
                self.movie_on.stop()
                self.label.setPixmap(self.pixmap_off)
                self.movie_on.jumpToFrame(0)
                self.movie_off.jumpToFrame(0)
            elif self.movie_off.currentFrameNumber() == self.movie_off.frameCount() - 1:
                self.current_state = "on"
                self.movie_off.stop()
                self.label.setPixmap(self.pixmap_on)
                self.movie_on.jumpToFrame(0)
                self.movie_off.jumpToFrame(0)

    def mousePressEvent(self, event):
        if self.current_state == "on":
            self.current_state = "transition"
            self.movie_on.start()
            self.label.setMovie(self.movie_on)
        elif self.current_state == "off":
            self.current_state = "transition"
            self.movie_off.start()
            self.label.setMovie(self.movie_off)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = AnimatedButton(r"./loading/d2n_15.gif",
                            r"./loading/n2d_15.gif")
    button.show()
    sys.exit(app.exec_())
