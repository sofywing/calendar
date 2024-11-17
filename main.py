import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
    

    def configure(self):
        self.ui.btn_start.clicked.connect(self.media_play)
        self.ui.btn_stop.clicked.connect(self.media_stop)
        self.ui.calendar.selectionChanged.connect(self.get_date)
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.ui.video)
        self.get_date()        

    def get_date(self):
        self.media_stop()
        self.day = self.ui.calendar.selectedDate().day()
        self.vid = QMediaContent(QUrl.fromLocalFile(f'Video\\{self.day}.avi'))
        self.media_player.setMedia(self.vid)
        if self.ui.cb_autoplay.isChecked():
            self.media_play()

    def media_play(self):
        self.media_player.play()

    def media_stop(self):
        self.media_player.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
